from typing import Any, Union, List, Iterable, Optional
from xmlrpc.client import DateTime
from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting
from saleae.data.timing import GraphTimeDelta
from enum import Enum
import sx127x_const as const



# High level analyzers must subclass the HighLevelAnalyzer class.
class SX127x(HighLevelAnalyzer):
    result_types = {
        'generic':  {'format': '{{data.info}}'},
        "address":  {"format": "{{data.rw}} {{data.reg}}"},
        "value":    {"format": "{{data.reg}}: {{data.value}}"},
        "payload":  {"format": "{{data.value}}"},
    }

    # ["LoRa", "FSK/OOK"]

    def __init__(self) -> None:
        self.__reg_write: bool = False
        self.__last_reg: Union[None, int] = None

    def __int_get(self, frame):
        mosi: bytes = frame.data["mosi"]
        miso: bytes = frame.data["miso"]
        return mosi[0], miso[0],

    def parse_content(data: int, last_reg: int, start_time: DateTime, end_time: DateTime):
        reg_name = const.SX127x_Reg_Name_get(last_reg)
        content = const.SX127x_Reg_Name_get(last_reg)
        if not content:
            return AnalyzerFrame(
                "value", start_time, end_time,
                {'value': f"0x{data:02X}", "reg": reg_name})
        bit_time = float(end_time - start_time) / 8
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
                    value = args.format(value)
                value = f"{name}{value}"
            else:
                value = f"0x{value:02X}"
            stime = start_time + (7 - msb) * bit_time
            etime = end_time - lsb * bit_time
            if reg_name:
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
        return ret

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
            # Clear local variables
            self.__last_reg = None
            return None

        try:
            mosi, miso = self.__int_get(frame)
        except IndexError:
            return None
        last_reg = self.__last_reg
        if last_reg is None:
            # Fist data packet is the req address
            reg_name = const.SX127x_Reg_Name_get(mosi)
            if reg_name:
                self.__last_reg = mosi
                self.__reg_write = (mosi & const.SX127X_SPI_REG_WRITE) == const.SX127X_SPI_REG_WRITE
                rw = "Write" if self.__reg_write else "Read"
                result = AnalyzerFrame(
                    "address", frame.start_time, frame.end_time,
                    {'rw': rw, "reg": reg_name})
            else:
                result = AnalyzerFrame(
                    "generic", frame.start_time, frame.end_time,
                    {'info': "REG??"})
        else:
            data = mosi if self.__reg_write else miso
            result = self.parse_content(
                data, last_reg, frame.start_time, frame.end_time)
            # Check if not FIFO write / read
            if last_reg != const.SX127X_REG_FIFO:
                self.__last_reg = last_reg + 1
        return result
