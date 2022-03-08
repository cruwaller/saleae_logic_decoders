from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting
from saleae.data.timing import GraphTimeDelta
from enum import Enum


class SmartAudio:
    SYNC_BYTE   = 0xAA
    HDR_BYTE    = 0x55
    BAUDRATE    = 4800

    class State(Enum):
        SYNC = 0
        HEADER = 1
        COMMAND = 2
        LENGTH = 3
        DATA = 4
        CRC = 5

    class Command(Enum):
        SA_CMD_NONE             = 0x00
        SA_CMD_GET_SETTINGS     = 0x01
        SA_CMD_SET_POWER        = SA_CMD_GET_SETTINGS + 1
        SA_CMD_SET_CHAN         = SA_CMD_GET_SETTINGS + 2
        SA_CMD_SET_FREQ         = SA_CMD_GET_SETTINGS + 3
        SA_CMD_SET_MODE         = SA_CMD_GET_SETTINGS + 4
        SA_CMD_GET_SETTINGS_V2  = 0x09,        # Response only
        SA_CMD_GET_SETTINGS_V21 = 0x11,

        # OpenVTx custom commands
        SA_CMD_BOOTLOADER       = 0x78,

    def __init__(self) -> None:
        self.clear()
        self._bit_time = 1. / self.BAUDRATE
        timeout = 2 * 11. / self.BAUDRATE
        self._time_to_clear = GraphTimeDelta(timeout) # 8N2
        # print(f"reset timeout: {timeout}")

    def clear(self) -> None:
        self._len_in = 0
        self._rxPacket = []
        self._state = self.State.SYNC

    def int_get(self, frame):
        return int.from_bytes(frame.data['data'], "little")

    def data_get(self) -> list:
        return [int.from_bytes(d.data['data'], "little") for d in self._rxPacket]

    def res_get(self, frame, info, bit=None):
        if bit is not None:
            # calc bit timing:
            offset = self._bit_time * (1 + bit[0])
            duration = self._bit_time * (1 + bit[1] - bit[0])
            start = self._rxPacket[frame[0]].start_time + offset
            end = start + duration
            return AnalyzerFrame(
                    "SmartAudio", start, end,
                    {'decoded': info})
        if type(frame) == tuple:
            return AnalyzerFrame(
                    "SmartAudio",
                    self._rxPacket[frame[0]].start_time,
                    self._rxPacket[frame[1]].end_time,
                    {'decoded': info})
        return AnalyzerFrame(
                "SmartAudio",
                frame.start_time,
                frame.end_time,
                {'decoded': info})

    def _calc_crc(self, start=0) -> int:
        poly = 0xD5
        crc = 0
        payload = self.data_get()[start:-1]
        for data in payload:
            crc ^= data
            for _ in range(8):
                if crc & 0x80:
                    crc = (crc << 1) ^ poly
                else:
                    crc = crc << 1
        return crc & 0xFF

    def _process_packet(self): # -> Any(AnalyzerFrame, None):
        result = []
        packet = self.data_get()
        command = (packet[2] >> 1)
        length = packet[3]
        if command == self.Command.SA_CMD_BOOTLOADER:
            command_str = "BOOTLOADER"
            if packet[4] == ord("S") and packet[5] == ord("S") and packet[6] == ord('T'):
                result.append(self.res_get((4, 6), "RESET"))
        elif command in [self.Command.SA_CMD_GET_SETTINGS,
                         self.Command.SA_CMD_GET_SETTINGS_V2,
                         self.Command.SA_CMD_GET_SETTINGS_V21]:
            command_str = "GET_SETTINGS"
            if length:
                if command == self.Command.SA_CMD_GET_SETTINGS:
                    command_str += " V1"
                elif command == self.Command.SA_CMD_GET_SETTINGS_V2:
                    command_str += " V2.0"
                elif command == self.Command.SA_CMD_GET_SETTINGS_V21:
                    command_str += " V2.1"
                result.append(self.res_get((4, 4), "Channel"))
                result.append(self.res_get((5, 5), "Power"))
                mode = packet[6]
                result.append(self.res_get((6, 6), "Mode"))
                fields = {0: "Freq mode", 1: "Pit mode", 2: "Pit inRange", 3: "Pit outRange", 4: "Unlocked"}
                for bit, info in fields.items():
                    if mode & (1 << bit):
                        result.append(self.res_get((4, 4), info, (bit, bit)))
                freq = packet[8]
                freq <<= 8
                freq += packet[7]
                result.append(self.res_get((7, 8), f"{freq}MHz"))
                result.append(self.res_get((9, 9), "Power raw"))

                if self.Command.SA_CMD_GET_SETTINGS_V21 <= command:
                    num_pwrs_str = "Num Powers"
                    num_pwrs = packet[10]
                    # Limit to packet len if wrong!
                    if (length - 7) < num_pwrs:
                        num_pwrs = (length - 7)
                        num_pwrs_str = "ERROR! " + num_pwrs_str
                    result.append(self.res_get((10, 10), num_pwrs_str))
                    for idx in range(11, (11 + num_pwrs)):
                        result.append(self.res_get((idx, idx), f"Level{idx-11}"))
        elif command == self.Command.SA_CMD_SET_POWER:
            command_str = "SET_POWER"
            pwr = packet[4] & 0x7F
            if packet[4] & 0x80:
                pwr = f"{pwr}dBm"
            else:
                pwr = f"{pwr}mW"
            result.append(self.res_get((4, 4), pwr))
        elif command == self.Command.SA_CMD_SET_CHAN:
            command_str = "SET_CHAN"
            chan = f"CH {packet[4]}"
            result.append(self.res_get((4, 4), chan))
        elif command == self.Command.SA_CMD_SET_FREQ:
            command_str = "SET_FREQ"
            freq = packet[4]
            freq <<= 8
            freq |= packet[5]
            result.append(self.res_get((4, 5), f"{freq}MHz"))
        elif command == self.Command.SA_CMD_SET_MODE:
            command_str = "SET_MODE"
            result.append(self.res_get((4, 4), "Mode"))
            mode = packet[4]
            fields = {0: "Pit inRange", 1: "Pit outRange", 2: "Pit clear", 3: "Unlocked"}
            for bit, info in fields.items():
                if mode & (1 << bit):
                    result.append(self.res_get((4, 4), info, (bit, bit)))
        else:
            command_str = "UNKNOWN"
        result.insert(0, self.res_get((2, 2), command_str))
        return result

    def process(self, frame: AnalyzerFrame): # -> Any(AnalyzerFrame, None):
        # reset if too long from last packet
        if self._rxPacket and self._time_to_clear < (frame.end_time - self._rxPacket[-1].end_time):
            self.clear()
        next_state = self.State.SYNC
        result = []
        data = int.from_bytes(frame.data['data'], "little")
        self._rxPacket.append(frame)
        if self._state == self.State.SYNC:
            if data == self.SYNC_BYTE:
                result = self.res_get(frame, "SYNC")
                next_state = self.State.HEADER
        elif self._state == self.State.HEADER:
            if data == self.HDR_BYTE:
                result = self.res_get(frame, "HDR")
                next_state = self.State.COMMAND
        elif self._state == self.State.COMMAND:
            result = self.res_get(frame, "CMD")
            next_state = self.State.LENGTH
        elif self._state == self.State.LENGTH:
            info = "LEN"
            length = self.int_get(frame)
            if length < 20:  # Check max len
                self._len_in = len(self._rxPacket) + length
                next_state = self.State.DATA
            else:
                info = "ERROR! " + info
            result = self.res_get(frame, info)
        elif self._state == self.State.DATA:
            if self._len_in < len(self._rxPacket):
                next_state = self.State.CRC
            else:
                next_state = self.State.DATA
        elif self._state == self.State.CRC:
            # Req CRC starts from index 0
            crc = data == self._calc_crc(start=0)
            if not crc:
                # Resp CRC starts from index 2
                crc = data == self._calc_crc(start=2)
            result.extend(self._process_packet())
            crc = "CRC" if crc else "CRC FAIL"
            result.append(self.res_get(frame, crc))
            next_state = self.State.SYNC

        self._state = next_state
        if next_state == self.State.SYNC:
            self.clear()
        return result


# High level analyzers must subclass the HighLevelAnalyzer class.
class SmartAudioHla(HighLevelAnalyzer):
    #my_string_settings = StringSetting()
    #my_number_settings = NumberSetting(min_value=0, max_value=100)
    #my_choices_settings = ChoicesSetting(choices=('A', 'B'))

    result_types = {
        'SmartAudio': {
            'format': '{{data.decoded}}'
        }
    }

    def __init__(self) -> None:
        ''' Initialize HLA. '''
        print("========== Smart Audio ==========")
        self.proto = SmartAudio()

    def decode(self, frame: AnalyzerFrame): # -> [AnalyzerFrame, None]:
        '''
        Process a frame from the input analyzer, and optionally return a single `AnalyzerFrame` or a list of `AnalyzerFrame`s.
        '''
        return self.proto.process(frame)
