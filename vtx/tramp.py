from random import choices
#from typing import Any
from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting
from saleae.data.timing import GraphTimeDelta
from enum import Enum


class TrampParser:
    SYNC_BYTE   = 0x0F
    MSG_SIZE    = 15
    BAUDRATE    = 9600

    class State(Enum):
        SYNC = 0
        DATA = 1
        CRC = 2

    def __init__(self) -> None:
        self.clear()
        timeout = 2 * 10. / self.BAUDRATE
        self._time_to_clear = GraphTimeDelta(timeout) # 8N1
        # print(f"reset timeout: {timeout}")

    def clear(self) -> None:
        self._rxPacket = []
        self._state = self.State.SYNC

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
                    "Tramp",
                    self._rxPacket[frame[0]].start_time,
                    self._rxPacket[frame[1]].end_time,
                    {'decoded': info})
        return AnalyzerFrame(
                "Tramp",
                frame.start_time,
                frame.end_time,
                {'decoded': info})

    def _calc_crc(self) -> int:
        data = self.data_get()[:-1]
        return sum(data) & 0xff

    def _process_packet(self): # -> Any(AnalyzerFrame, None):
        result = []
        packet = self.data_get()[1:]
        if packet[0] == ord('F'): # Freq
            freq = packet[2]
            freq <<= 8
            freq |= packet[1]
            result = [
                self.res_get((1, 1), f"FREQ"),
                self.res_get((2, 3), f"{freq}MHz")]
        elif packet[0] == ord('P'): # Power
            mW = packet[2]
            mW <<= 8
            mW |= packet[1]
            result = [
                self.res_get((1, 1), f"PWR"),
                self.res_get((2, 3), f"{mW}mW")]
        elif packet[0] == ord('I'): # Pitmode
            pitmode = ["ON", "OFF"][bool(packet[1])]
            result = [
                self.res_get((1, 1), f"PIT"),
                self.res_get((2, 3), f"{pitmode}")]
        elif packet[0] == ord('r'): # Max min freq and power packet
            result.append(self.res_get((1, 1), f"LIMITS"))
            temp = packet[2]
            temp <<= 8
            temp |= packet[1]
            result.append(self.res_get((2, 3), f"f min {temp}MHz"))
            temp = packet[4]
            temp <<= 8
            temp |= packet[3]
            result.append(self.res_get((4, 5), f"f max {temp}MHz"))
            temp = packet[6]
            temp <<= 8
            temp |= packet[5]
            result.append(self.res_get((6, 7), f"P max {temp}mW"))
        elif packet[0] == ord('v'): # Verify
            result.append(self.res_get((1, 1), f"STATUS"))
            res = "VERIFY: "
            temp = packet[2]
            temp <<= 8
            temp |= packet[1]
            result.append(self.res_get((2, 3), f"f {temp}MHz"))
            temp = packet[4]
            temp <<= 8
            temp |= packet[3]
            result.append(self.res_get((4, 5), f"P {temp}mW"))
            result.append(self.res_get((6, 6), f"Mode"))
            temp = ["ON", "OFF"][bool(packet[6])]
            result.append(self.res_get((7, 7), f"Pit {temp}"))
            temp = packet[8]
            temp <<= 8
            temp |= packet[7]
            result.append(self.res_get((8, 9), f"P real {temp}mW"))
        elif packet[0] == ord('s'): # Temperature
            temp = packet[6]
            temp <<= 8
            temp |= packet[5]
            if temp & 0x8000:
                temp = -1 * (temp & 0x7fff)
            result = [
                self.res_get((1, 1), f"TEMP"),
                self.res_get((6, 7), f"{temp}C")]
        elif packet[0] == ord('R'): # Reboot (bootloader)
            if packet[1] == ord("S") and packet[2] == ord('T'):
                result = [self.res_get((1, 3), "BOOTLOADER")]
        else:
            result = [self.res_get((1, 1), "UNKNOWN")]
        return result

    def process(self, frame: AnalyzerFrame): # -> Any(AnalyzerFrame, None):
        # reset if too long from last packet
        if self._rxPacket and self._time_to_clear < (frame.end_time - self._rxPacket[-1].end_time):
            self.clear()
        result = []
        data = int.from_bytes(frame.data['data'], "little")
        self._rxPacket.append(frame)
        if self._state == self.State.SYNC:
            if data == self.SYNC_BYTE:
                self._state = self.State.DATA
                result = self.res_get(frame, "SYNC")
            else:
                self.clear()
        elif self._state == self.State.DATA:
            # result = self.res_get(frame, "Data")
            if (self.MSG_SIZE - 1) <= len(self._rxPacket):
                self._state = self.State.CRC
        elif self._state == self.State.CRC:
            crc = data == self._calc_crc()
            result.extend(self._process_packet())
            self.clear()
            crc = "CRC" if crc else "CRC FAIL"
            result.append(self.res_get(frame, crc))
        return result


# High level analyzers must subclass the HighLevelAnalyzer class.
class TrampHla(HighLevelAnalyzer):
    #my_string_settings = StringSetting()
    #my_number_settings = NumberSetting(min_value=0, max_value=100)
    #my_choices_settings = ChoicesSetting(choices=('A', 'B'))

    result_types = {
        'Tramp': {
            'format': '{{data.decoded}}'
        }
    }

    def __init__(self) -> None:
        ''' Initialize HLA. '''
        print("========== Tramp ==========")
        self.proto = TrampParser()

    def decode(self, frame: AnalyzerFrame): # -> [AnalyzerFrame, None]:
        '''
        Process a frame from the input analyzer, and optionally return a single `AnalyzerFrame` or a list of `AnalyzerFrame`s.
        '''
        return self.proto.process(frame)
