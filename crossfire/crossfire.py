from typing import Any, Union, List
from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting
from saleae.data.timing import GraphTimeDelta, GraphTime
from enum import Enum
import const
import msp


def __get_value(data: List[int], cnt: int):
    value = 0
    for _ in range(cnt):
        value <<= 8
        value += data.pop(0)
    return value


def __parse_value_list(params: List[tuple], data: List[int], res_gen, offset:int=3, resolver=None):
    res = []
    for info, size in params:
        negat = size < 0
        size = abs(size)
        value = __get_value(data, size)
        if negat and value & (1 << (size - 1)):
            value -= (1 << size)
        if resolver is not None:
            value = resolver(value)
        res.append(res_gen((offset, offset+size-1), f"{info}: {value}"))
        offset += size
    return offset, res


def __parse_ext_header(data: List[int], res_gen, offset:int=3):
    params = [("Dest", 1), ("Orig", 1)]
    return __parse_value_list(params, data, res_gen, offset, const.CRSF_ADDR_2_NAME)


def parser_gps(data: List, res_gen, offset:int=3):
    params = [
        ("Lat", 4), ("Long", 4),
        ("Speed", 2), ("Heading", 2), ("Altitude", 2),
        ("Satellites", 1),
    ]
    offset, res = __parse_value_list(params, data, res_gen, offset)
    return res


def parser_battery_sensor(data: List, res_gen, offset:int=3):
    res = []
    val = float(__get_value(data, 2)) / 10.
    res.append(res_gen((offset, offset+1), f"Voltage: {val}V"))
    offset += 2
    val = float(__get_value(data, 2)) / 10.
    res.append(res_gen((offset, offset+1), f"Current: {val}A"))
    offset += 2
    val = __get_value(data, 3)
    res.append(res_gen((offset, offset+2), f"Capacity: {val}mAh"))
    offset += 3
    res.append(res_gen((offset, offset), f"Remaining: {data.pop(0)}%"))
    return res

def parser_link_stat(data: List, res_gen, offset:int=3):
    params = [
        ("UL RSSI 1", -1),
        ("UL RSSI 2", -1),
        ("UL LQ", 1),
        ("UL SNR", -1),
        ("Antenna", 1),
        ("RF Mode", 1),
        ("UL PWR Index", 1),
        ("DL RSSI", -1),
        ("DL LQ", 1),
        ("DL SNR", -1),
    ]
    offset, res = __parse_value_list(params, data, res_gen, offset)
    return res

def parser_link_stat_elrs(data: List, res_gen, offset:int=3):
    params = [
        ("UL RSSI", -1),
        ("UL LQ", 1),
        ("UL SNR", -1),
        ("RF Mode", 1),
    ]
    offset, res = __parse_value_list(params, data, res_gen, offset)
    return res

def parser_link_stat_rx(data: List, res_gen, offset:int=3):
    params = [
        ("DL RSSI", -1),
        ("DL RSSI %", 1),
        ("DL LQ", 1),
        ("DL SNR", -1),
        ("UL TX Pwr", 1),
    ]
    offset, res = __parse_value_list(params, data, res_gen, offset)
    return res

def parser_link_stat_tx(data: List, res_gen, offset:int=3):
    params = [
        ("UL RSSI", -1),
        ("UL RSSI %", 1),
        ("UL LQ", 1),
        ("UL SNR", -1),
        ("DL TX Pwr", 1),
        ("UL FPS", 1),
    ]
    offset, res = __parse_value_list(params, data, res_gen, offset)
    return res

def parser_radio_id(data: List, res_gen, offset:int=3):
    offset, res = __parse_ext_header(data, res_gen, offset)

    cmd_id = data.pop(0)
    res.append(res_gen((offset, offset), const.CRSF_RadioID_Subtype_2_Name(cmd_id)))
    offset += 1

    if cmd_id == const.CRSF_RADIO_ID_SUBTYPE_TIMING_SYNC:
        params = [("Interval", 4), ("Offset", -4)]
        offset, res_tmp = __parse_value_list(params, data, res_gen, offset)
    else:
        res_tmp = [res_gen((offset, offset+len(data)-1), f"Payload")]
    res.extend(res_tmp)
    return res

def parser_attitude(data: List, res_gen, offset:int=3):
    def resolver(val):
        return val / 10.
    params = [("Pitch", -2), ("Roll", -2), ("Yaw", -2)]
    offset, res = __parse_value_list(params, data, res_gen, offset, resolver)
    return res

def parser_flight_mode(data: List, res_gen, offset:int=3):
    idx = 0
    mode = "Flight mode: "
    for byte in data:
        idx += 1
        if byte == 0:
            break
        mode += chr(byte)
    res = [res_gen((offset, offset+idx-1), mode)]
    return res

def parser_ping(data: List, res_gen, offset:int=3):
    res = [res_gen((offset, offset+len(data)-1), f"Ping message")]
    return res

def parser_info(data: List, res_gen, offset:int=3):
    # dest + orig
    offset, res = __parse_ext_header(data, res_gen, offset)
    # size = len(data) - 12 - 2
    size = 0
    name = "Name: "
    for byte in data:
        size += 1
        if byte == 0:
            break
        name += chr(byte)
    res.append(res_gen((offset, offset+size-1), name))
    offset += size
    res.append(res_gen((offset, offset+12-1), f"NULL"))
    offset += 12
    res.append(res_gen((offset, offset), f"Max MSP Parameter"))
    offset += 1
    res.append(res_gen((offset, offset), f"Parameter version"))
    return res

def parser_parameter_setting_entry(data: List, res_gen, offset:int=3):
    res = [res_gen((offset, offset+len(data)-1), f"Paramter setting entry message")]
    return res

def parser_parameter_read(data: List, res_gen, offset:int=3):
    res = [res_gen((offset, offset+len(data)-1), f"Paramter Read message")]
    return res

def parser_parameter_write(data: List, res_gen, offset:int=3):
    res = [res_gen((offset, offset+len(data)-1), f"Paramter Write message")]
    return res

def parser_command(data: List, res_gen, offset:int=3):
    # dest + orig
    offset, res = __parse_ext_header(data, res_gen, offset)
    command = data.pop(0)
    res.append(res_gen((offset, offset), const.CRSF_SUBCMD_2_NAME(command)))
    offset += 1
    if command == const.CRSF_COMMAND_SUBCMD_GENERAL:
        sub_cmd = data.pop(0)
        res.append(res_gen((offset, offset), const.CRSF_SUBCMD_2_NAME(sub_cmd)))
        offset += 1
        if sub_cmd == const.CRSF_COMMAND_SUBCMD_GENERAL_CRSF_SPEED_PROPOSAL:
            id = data.pop(0)
            res.append(res_gen((offset, offset), f"Port ID"))
            offset += 1
            baud = __get_value(data, 4)
            res.append(res_gen((offset, offset+3), f"Baudrate {baud}"))
            offset += 4
        elif sub_cmd == const.CRSF_COMMAND_SUBCMD_GENERAL_CRSF_SPEED_RESPONSE:
            id = data.pop(0)
            res.append(res_gen((offset, offset), f"Port ID"))
            offset += 1
            status = data.pop(0)
            res.append(res_gen((offset, offset), f"{['FAIL','SUCCESS'][bool(status)]}"))
            offset += 1
    return res

def parser_parameter_msp_req(data: List, res_gen, offset:int=3, resp:bool=False):
    offset, res = __parse_ext_header(data, res_gen, offset)
    # [0] header: flags + seq&0xF
    header = data.pop(0)
    res.append(res_gen((offset, offset), f"Seq: {header & 0xF}", (0, 3)))
    res.append(res_gen((offset, offset), ["Continue", "Start"][bool(header & (1 << 4))], (4, 4)))
    res.append(res_gen((offset, offset), "Version", (5, 6)))
    offset += 1
    if resp or header & (1 << 4):
        # Start:
        #    [1] payload size
        #    [2] function
        _ = data.pop(0)
        res.append(res_gen((offset, offset), f"Size"))
        offset += 1
        func = msp.MSP_id_2_name(data.pop(0))
        res.append(res_gen((offset, offset), f"Function: {func}"))
        offset += 1
    # REQ:  [3... 7] payload / crc
    # RESP: [3...57] payload / crc
    res.append(res_gen((offset, offset+len(data)-1), f"Payload"))
    return res

def parser_parameter_msp_resp(data: List, res_gen, offset:int=3):
    return parser_parameter_msp_req(data, res_gen, offset, resp=True)

def parser_parameter_displayport_cmd(data: List, res_gen, offset:int=3):
    offset, res = __parse_ext_header(data, res_gen, offset)
    subcmd = data.pop(0)
    res.append(res_gen((offset, offset), const.CRSF_Displayport_Subcmd_2_Name(subcmd)))
    offset += 1
    if subcmd == const.CRSF_DISPLAYPORT_SUBCMD_OPEN:
        params = [("Rows", 1), ("Cols", 1)]
        offset, res_tmp = __parse_value_list(params, data, res_gen, offset)
        res.extend(res_tmp)
    res.append(res_gen((offset, offset+len(data)-1), f"Payload"))
    return res


CRSF_FRAME_PARSERS = {
    const.CRSF_FRAMETYPE_GPS: parser_gps,
    const.CRSF_FRAMETYPE_BATTERY_SENSOR: parser_battery_sensor,
    const.CRSF_FRAMETYPE_LINK_STATISTICS: parser_link_stat,
    const.CRSF_FRAMETYPE_LINK_STATISTICS_ELRS: parser_link_stat_elrs,
    const.CRSF_FRAMETYPE_RADIO_ID: parser_radio_id,
    #const.CRSF_FRAMETYPE_RC_CHANNELS_PACKED: parser_channels_packed,
    #const.CRSF_FRAMETYPE_SUBSET_RC_CHANNELS_PACKED: parser_channels_packed_susbset,
    const.CRSF_FRAMETYPE_LINK_STATISTICS_RX: parser_link_stat_rx,
    const.CRSF_FRAMETYPE_LINK_STATISTICS_TX: parser_link_stat_tx,
    const.CRSF_FRAMETYPE_ATTITUDE: parser_attitude,
    const.CRSF_FRAMETYPE_FLIGHT_MODE: parser_flight_mode,
    const.CRSF_FRAMETYPE_DEVICE_PING: parser_ping,
    const.CRSF_FRAMETYPE_DEVICE_INFO: parser_info,
    const.CRSF_FRAMETYPE_PARAMETER_SETTINGS_ENTRY: parser_parameter_setting_entry,
    const.CRSF_FRAMETYPE_PARAMETER_READ: parser_parameter_read,
    const.CRSF_FRAMETYPE_PARAMETER_WRITE: parser_parameter_write,
    const.CRSF_FRAMETYPE_COMMAND: parser_command,

    const.CRSF_FRAMETYPE_MSP_REQ: parser_parameter_msp_req,
    const.CRSF_FRAMETYPE_MSP_RESP: parser_parameter_msp_resp,
    const.CRSF_FRAMETYPE_MSP_WRITE: parser_parameter_msp_req,

    const.CRSF_FRAMETYPE_DISPLAYPORT_CMD: parser_parameter_displayport_cmd,
}


class Crsf:
    BAUDRATE    = 400000

    class State(Enum):
        SYNC = 0
        LENGTH = 1
        DATA = 3
        CRC = 4

    def __init__(self, rc_rate, parsing_type) -> None:
        self.clear()
        self._bit_time = 1. / self.BAUDRATE
        self._time_to_clear = GraphTimeDelta(30. * self._bit_time)
        self._first_packet_time = None
        self._rc_total = 0
        self._rc_total_missed = 0
        if rc_rate:
            self._rc_rate_inv = 1. / rc_rate
            print(f"RC timing: {self._rc_rate_inv}s")
        else:
            self._rc_rate_inv = 0
        self._rc_last_valid = None
        self._output_missing_rc = parsing_type == "Missing RC"

        # Temporary values to avoid Logic software issue
        self._byte_sync = None
        self._byte_len = None
        self._byte_command = None

        global CRSF_FRAME_PARSERS
        CRSF_FRAME_PARSERS.update({
            const.CRSF_FRAMETYPE_RC_CHANNELS_PACKED: self.parser_channels_packed,
            const.CRSF_FRAMETYPE_SUBSET_RC_CHANNELS_PACKED: self.parser_channels_packed_susbset,
        })

    def clear(self) -> None:
        self._crc_in = 0
        self._len_in = 0
        self._rxPacket = []
        self._state = self.State.SYNC

    updated = False
    def update_timeout(self, frame):
        if self.updated:
            return
        self.updated = True
        self._bit_time = ((frame.end_time - frame.start_time) / 9.5)
        # print(f"bit time: {self._bit_time}, baud {1./float(self._bit_time)}")
        self._time_to_clear = GraphTimeDelta(30. * float(self._bit_time))

    def int_get(self, frame):
        return int.from_bytes(frame.data['data'], "little")

    def data_get(self) -> List[int]:
        return [int.from_bytes(d.data['data'], "little") for d in self._rxPacket]

    def res_get(self, frame: Union[tuple, AnalyzerFrame], info: str,
                bit: Union[None, tuple]=None,
                start=None, end=None) -> AnalyzerFrame:
        if bit is not None:
            # calc bit timing:
            offset = self._bit_time * (1 + bit[0])  # 1 start bit
            duration = self._bit_time * (1 + bit[1] - bit[0])
            start = self._rxPacket[frame[0]].start_time + offset
            end = start + duration
            return AnalyzerFrame("crsf", start, end, {'decoded': info})
        if type(frame) == tuple:
            return AnalyzerFrame(
                    "crsf",
                    self._rxPacket[frame[0]].start_time,
                    self._rxPacket[frame[1]].end_time,
                    {'decoded': info})
        return AnalyzerFrame(
                "crsf",
                frame.start_time,
                frame.end_time,
                {'decoded': info})

    def _calc_crc(self, data: int, crc: int, poly:int = const.CRSF_GEN_POLY) -> int:
        crc ^= data
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ poly
            else:
                crc = crc << 1
        return crc & 0xFF

    def _calc_crc_frame(self, poly:int = const.CRSF_GEN_POLY) -> int:
        payload = self.data_get()[2:-1]
        crc = 0
        for data in payload:
            crc = self._calc_crc(data, crc, poly)
        return crc

    def parser_channels(self, data: List, res_gen, offset:int=3, bits_per_ch:int=11, channel:int=0):
        res = []
        bits_per_ch_mask = (1 << bits_per_ch) - 1
        value = bits_read = 0
        bit_time = self._bit_time
        rx_packets = self._rxPacket[offset:(offset + len(data))]  # Ignore CRC
        start_time = rx_packets[0].start_time
        extension = 0
        for packet in rx_packets:
            extension += float(bit_time)
            value += self.int_get(packet) << bits_read
            bits_read += 8
            while bits_per_ch <= bits_read:
                ch_val = value & bits_per_ch_mask
                end_time = start_time + (bit_time * bits_per_ch) + GraphTimeDelta(extension)
                extension = 0
                frame = AnalyzerFrame("crsf", start_time, end_time, {'decoded': f"CH{channel}: {ch_val}"})
                res.append(frame)
                start_time = end_time
                value >>= bits_per_ch
                bits_read -= bits_per_ch
                channel += 1
            extension += float(bit_time)
        return res

    # 2022-03-14T08:29:40.041935920000Z
    # 2022-03-14T08:29:40.041935920000Z
    # 2022-03-14T08:29:40.042935920000Z

    def missing_rc_packet_check(self, start_time):
        self._rc_total += 1
        result = []
        rc_rate_inv = self._rc_rate_inv
        last = self._rc_last_valid
        if rc_rate_inv and last is not None:
            diff = float(start_time - last)
            if (1.5 * rc_rate_inv) <= diff:
                missed = int((diff + rc_rate_inv / 2) // rc_rate_inv) - 1
                self._rc_total_missed += missed
                #print(f"missed {missed}, from 1st {float(last - self._first_packet_time):.6f}, "
                #      f"missing: {self._rc_total_missed} of {self._rc_total}")
                if self._output_missing_rc:
                    for idx in range(missed):
                        # Calculate missed slot
                        last += GraphTimeDelta(rc_rate_inv)
                        # Frames must be ordered in time!!
                        result.append(AnalyzerFrame(
                            "crsf",
                            last,
                            last + GraphTimeDelta(20. / 1E6), # 30us
                            {'decoded': f"MISSING.{idx+1}"}))
        # This is a workaround. Logic requires AnalyzerFrames to be in ordered (time domain)
        if self._output_missing_rc:
            result.append(self._byte_sync)
            result.append(self._byte_len)
            result.append(self._byte_command)
        self._rc_last_valid = start_time
        return result

    def parser_channels_packed(self, data: List, res_gen, offset:int=3, bits_per_ch:int=11, channel:int=0):
        res = self.missing_rc_packet_check(self._rxPacket[0].start_time)
        if len(data) == 9:
            # ELRS protocol message (length = 9B)
            ch_bytes = 4 * 12 // 8
            res.extend(self.parser_channels(data[:ch_bytes], res_gen, offset, bits_per_ch=12, channel=0))
            offset += ch_bytes
            res.extend(self.parser_channels(data[ch_bytes:], res_gen, offset, bits_per_ch=3, channel=4))
            return res
        # CRSF v2 protocol message (length = 22B)
        res.extend(self.parser_channels(data, res_gen, offset, bits_per_ch, channel))
        return res

    def parser_channels_packed_susbset(self, data: List, res_gen, offset:int=3):
        # CRSF v3 protocol message (variable length)
        res = self.missing_rc_packet_check(self._rxPacket[0].start_time)
        config_byte = self._rxPacket[offset]
        start_ch = config_byte & 0x1F
        bits_per_ch = [10, 11, 12, 13][(config_byte >> 5) & 0x3]
        res.append(res_gen((offset,offset), f"start: {start_ch}", (0, 4)))
        res.append(res_gen((offset,offset), f"bits: {bits_per_ch}", (5, 6)))
        res.extend(self.parser_channels(data, res_gen, offset + 1, bits_per_ch, start_ch))
        return res

    def parser_default(self, data: List, res_gen, offset:int=3):
        return [res_gen((offset, offset+len(data)-1), "DATA")]

    def _process_packet(self) -> List[Union[AnalyzerFrame, None]]:
        result = []
        frame = self.data_get()[2:-1]  # Skip hdr bytes (2) and crc (1)
        frame_type = frame[0]
        self._byte_command = self.res_get((2, 2), const.CRSF_FRAMETYPE_2_NAME(frame_type))
        if not self._output_missing_rc:
            result.append(self._byte_command)
        # Parse data if parser defined
        parser = CRSF_FRAME_PARSERS.get(frame_type, self.parser_default)
        result.extend(parser(frame[1:], self.res_get, 3))  # skip type
        return result

    def process(self, frame: AnalyzerFrame) -> List[AnalyzerFrame]:
        if self._first_packet_time is None:
            self._first_packet_time = frame.start_time
            # print(f"First packet at {frame.start_time}")
        # reset if too long from last packet
        if self._rxPacket and self._time_to_clear < (frame.start_time - self._rxPacket[-1].end_time):
            self.clear()
        result = []
        data = self.int_get(frame)
        self._rxPacket.append(frame)

        # Calculate baudrate based on frame timing
        self.update_timeout(frame)

        if self._state == self.State.SYNC:
            if data == const.CRSF_ADDRESS_CRSF_RECEIVER or \
                    data == const.CRSF_ADDRESS_CRSF_TRANSMITTER or \
                    data == const.CRSF_SYNC_BYTE:
                self._state = self.State.LENGTH
                self._byte_sync = self.res_get(frame, "SYNC")
                if not self._output_missing_rc:
                    result.append(self._byte_sync)
            else:
                self.clear()
        elif self._state == self.State.LENGTH:
            self._byte_len = self.res_get(frame, "LEN")
            if not self._output_missing_rc:
                result.append(self._byte_len)
            if const.CRSF_FRAME_HEADER_BYTES <= data <= const.CRSF_PAYLOAD_SIZE_MAX:
                self._len_in = const.CRSF_FRAME_START_BYTES + data - 1
                self._state = self.State.DATA
            else:
                self.clear()
        elif self._state == self.State.DATA:
            self._crc_in = self._calc_crc(data, self._crc_in)
            if self._len_in <= len(self._rxPacket):
                self._state = self.State.CRC
        elif self._state == self.State.CRC:
            result.extend(self._process_packet())
            crc = "CRC" if data == self._crc_in else "CRC FAIL"
            result.append(self.res_get(frame, crc))
            self.clear()
        return result


# High level analyzers must subclass the HighLevelAnalyzer class.
class CrossfireHla(HighLevelAnalyzer):
    result_types = {
        'crsf': {
            'format': '{{data.decoded}}'
        }
    }
    exp_rc_rate = NumberSetting(min_value=0, max_value=2000)
    parsing_type = ChoicesSetting(['Missing RC', 'Content'])

    def __init__(self) -> None:
        ''' Initialize HLA. '''
        print("========== CRSF ==========")
        print(f"Expected RC rate: {self.exp_rc_rate}")
        print(f"Parsin type: '{self.parsing_type}'")
        self.proto = Crsf(self.exp_rc_rate, self.parsing_type)

    def decode(self, frame: AnalyzerFrame) -> List[AnalyzerFrame]:
        '''
        Process a frame from the input analyzer, and optionally return a single `AnalyzerFrame` or a list of `AnalyzerFrame`s.
        '''
        return self.proto.process(frame)
