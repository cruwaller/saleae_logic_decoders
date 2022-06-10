from typing import Any, Union, List, Iterable, Optional
from xmlrpc.client import DateTime
from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting
from saleae.data.timing import GraphTimeDelta
from enum import Enum
import re
import sx128x_const as const



# High level analyzers must subclass the HighLevelAnalyzer class.
class SX128x(HighLevelAnalyzer):
    result_types = {
        "command":  {"format": "{{data.cmd}}"},
        "value":    {"format": "{{data.reg}}: {{data.value}}"},
        "payload":  {"format": "{{data.value}}"},
    }

    class State(Enum):
        NONE = 0
        COMMAND = 1
        ADDRESS1 = 2
        ADDRESS2 = 3
        NOP = 4
        OFFSET = 5
        PAYLOAD = 6
        VALUE = 7

    # xo_freq = NumberSetting(min_value=20E6, max_value=100E6, label="XTAL freq (default: 52MHz)")

    def __init__(self) -> None:
        # const.SX128x_XO_Freq_set(self.xo_freq)
        self.__state = self.State.NONE
        self.__frames_tmp: List = []
        self.__address_int: Optional[int] = 0
        self.__read_cmd: bool = False
        self.__opcode: Optional[int] = None
        self.__packet_type = const.SX128x_PKT_TYPE_INVALID

    def __clear(self):
        self.__opcode = None
        self.__frames_tmp.clear()
        self.__state = self.State.NONE

    def __int_get(self, frame):
        mosi: bytes = frame.data["mosi"]
        miso: bytes = frame.data["miso"]
        return mosi[0], miso[0],

    idx_byte = 0
    def parse_content(self, data: int, opcode: int, start_time: DateTime,
                      end_time: DateTime, reg_name: str=""):
        if not reg_name:
            _, reg_name = const.SX128x_Command_Name_get(opcode)
        contents = const.SX128x_Opcode_Content_get(opcode, self.__packet_type)
        if not contents:
            return AnalyzerFrame(
                "value", start_time, end_time,
                {'value': f"0x{data:02X}", "reg": reg_name})
        try:
            content = contents[self.idx_byte]
        except IndexError:
            # Parsing error
            print(f"  WTF!! opcode {opcode} type: {self.__packet_type}, offset {self.idx_byte}")
            return None
        _bytes = ((content[0][0] + 8) // 8)
        if 1 < _bytes:
            frame = self.__frames_tmp
            frame.append((start_time, end_time, data))
            # Chekc if pieces are still needed
            if len(frame) < _bytes:
                return None
            # Merge data
            start_time, _, data = frame.pop(0)
            end_time = frame[-1][1]
            for _, _, val in frame:
                data <<= 8
                data += val
            frame.clear()
        if opcode == const.SX1280_RADIO_SET_PACKETTYPE:
            self.__packet_type = const.SX128x_Pkt_Type_get(data)
        bit_size = _bytes * 8
        bit_time = GraphTimeDelta(float(end_time - start_time) / bit_size)
        ret = []
        for msb, lsb, args in content:
            value_mask = sum([0x1 << x for x in range(lsb, msb+1)])
            value = (data & value_mask) >> lsb
            bits = msb - lsb + 1
            if type(args) == list:
                try:
                    value = args[value]
                except IndexError:
                    value = "??"
                value = f"{value}"
            elif type(args) == dict:
                name = args.get("name", "")
                if name:
                    name += ": "
                _eval = args.get("eval")
                if _eval:
                    value = eval(_eval.format(value))
                values = args.get("values")
                if values:
                    if type(values) == list:
                        try:
                            value = values[value]
                        except IndexError:
                            value = "??"
                    else:
                        value = values.get(value, "??")
                _fmt = args.get("fmt")
                if _fmt:
                    if "d}" in _fmt:
                        # Convert to signed
                        if value & (0x1 << (bits - 1)):
                            value -= (1 << bits)
                    value = _fmt.format(value)
                value = f"{name}{value}"
            elif type(args) == str:
                _fmt = re.search(r'(?<={).*}', args)
                if _fmt:
                    _fmt = _fmt.group(0)
                    if "d}" in _fmt:
                        # Convert to signed
                        if value & (0x1 << (bits - 1)):
                            value -= (1 << bits)
                    value = args.format(value)
                else:
                    value = args
            else:
                value = f"{value:#X}"
            stime = start_time + bit_time * (bit_size - 1 - msb)
            etime = stime + bit_time * (msb - lsb + 1)
            if reg_name and self.idx_byte == 0:
                res = AnalyzerFrame(
                    "value",
                    stime, etime,
                    {'value': f"{value}", "reg": reg_name})
                reg_name = ""
            else:
                res = AnalyzerFrame(
                    "payload",
                    stime, etime,
                    {'value': f"{value}"})
            ret.append(res)
        self.idx_byte += 1
        return ret

    def decode_first(self, mosi: int, miso: int, start_time: DateTime, end_time: DateTime):
        # Parse Opcode (MOSI)
        is_read_cmd, reg_name = const.SX128x_Command_Name_get(mosi)
        self.__read_cmd = is_read_cmd
        self.__opcode = mosi
        if mosi in [const.SX1280_RADIO_READ_REGISTER, const.SX1280_RADIO_WRITE_REGISTER]:
            # Address is 16b
            self.__state = self.State.ADDRESS1
            self.__frames_tmp.clear()
        elif mosi in [const.SX1280_RADIO_WRITE_BUFFER, const.SX1280_RADIO_READ_BUFFER]:
            self.__state = self.State.OFFSET
        self.idx_byte = 0
        # Parse status byte (MISO)
        return self.parse_content(miso, const.SX1280_RADIO_GET_STATUS, start_time, end_time, reg_name=reg_name)

    def decode(self, frame: AnalyzerFrame
                ) -> Optional[Union[Iterable[AnalyzerFrame], AnalyzerFrame]]:
        '''
        https://support.saleae.com/extensions/analyzer-frame-types/spi-analyzer
        frame.type:
            'enable' = CS enabled
            'disable' = CS disabled
            'result' = data["miso"] or data["mosi"]
            'error' = Clock failure
        '''
        if frame.type != "result":
            self.__clear()
            return None

        try:
            mosi, miso = self.__int_get(frame)
        except IndexError:
            self.__clear()
            return None

        if self.__state == self.State.ADDRESS1:
            self.__address_int = mosi << 8
            self.__frames_tmp.append(frame)
            self.__state = self.State.ADDRESS2
            return
        elif self.__state == self.State.ADDRESS2:
            self.__address_int += mosi
            self.__frames_tmp.append(frame)
            self.__state = self.State.NOP if self.__read_cmd else self.State.PAYLOAD
            name = const.SX128x_Register_Name_get(self.__address_int, "Address")
            info = AnalyzerFrame(
                "command", self.__frames_tmp[0].start_time, frame.end_time,
                {"cmd": f"Address: {name}"})
            self.__frames_tmp.clear()
            return info
        elif self.__state == self.State.NOP:
            self.__state = self.State.PAYLOAD
            info = AnalyzerFrame(
                "command", frame.start_time, frame.end_time,
                {"cmd": "NOP"})
            return info
        elif self.__state == self.State.OFFSET:
            self.__state = self.State.NOP if self.__read_cmd else self.State.PAYLOAD
            self.__address_int = mosi
            info = AnalyzerFrame(
                "command", frame.start_time, frame.end_time,
                {"cmd": f"Offset"})
            return info
        elif self.__state == self.State.PAYLOAD:
            address = self.__address_int
            name = const.SX128x_Register_Name_get(address, f"0x{address:04X}")
            #data = miso if self.__read_cmd else mosi
            #info = self.parse_content(
            #    data, address, frame.start_time, frame.end_time, name)
            info = AnalyzerFrame(
                "command", frame.start_time, frame.end_time,
                {"cmd": name})
            self.__address_int = address + 1
            return info

        opcode = self.__opcode
        if opcode is None:
            # Fist data packet is the command
            result = self.decode_first(mosi, miso, frame.start_time, frame.end_time)
            self.idx_byte = 0
        else:
            data = miso if self.__read_cmd else mosi
            result = self.parse_content(
                data, opcode, frame.start_time, frame.end_time)
        return result
