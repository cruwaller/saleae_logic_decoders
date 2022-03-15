
CRSF_GEN_POLY = 0xD5
CRSF_CMD_POLY = 0xBA

CRSF_NUM_CHANNELS = 16         # Number of input channels

CRSF_SYNC_BYTE = 0xC8

CRSF_PAYLOAD_SIZE_MAX   = 62

CRSF_FRAME_START_BYTES  = 2 # address + len (start of the CRSF frame, not counted to frame len)
CRSF_FRAME_HEADER_BYTES = 2 # type + crc
CRSF_FRAME_SIZE_MAX     = (CRSF_PAYLOAD_SIZE_MAX + CRSF_FRAME_START_BYTES)

CRSF_MSP_FRAME_HEADER_BYTES = 4 # type, dest, orig, crc

def CRSF_FRAME_SIZE(payload_size):
    return ((payload_size) + CRSF_FRAME_HEADER_BYTES) # See crsf_header_t.frame_size
def CRSF_EXT_FRAME_SIZE(payload_size):
    return (CRSF_FRAME_SIZE(payload_size) + CRSF_FRAME_START_BYTES)

def CRSF_MSP_FRAME_SIZE(payload_size):
    return (CRSF_FRAME_SIZE(payload_size) + CRSF_MSP_FRAME_HEADER_BYTES)

CRSF_FRAMETYPE_GPS = 0x02
CRSF_FRAMETYPE_BATTERY_SENSOR = 0x08
CRSF_FRAMETYPE_LINK_STATISTICS = 0x14
CRSF_FRAMETYPE_LINK_STATISTICS_ELRS = 0x15
CRSF_FRAMETYPE_RC_CHANNELS_PACKED = 0x16
CRSF_FRAMETYPE_SUBSET_RC_CHANNELS_PACKED = 0x17
CRSF_FRAMETYPE_LINK_STATISTICS_RX = 0x1C
CRSF_FRAMETYPE_LINK_STATISTICS_TX = 0x1D
CRSF_FRAMETYPE_ATTITUDE = 0x1E
CRSF_FRAMETYPE_FLIGHT_MODE = 0x21
# Extended Header Frames, range: 0x28 to 0x96
CRSF_FRAMETYPE_DEVICE_PING = 0x28
CRSF_FRAMETYPE_DEVICE_INFO = 0x29
CRSF_FRAMETYPE_PARAMETER_SETTINGS_ENTRY = 0x2B
CRSF_FRAMETYPE_PARAMETER_READ = 0x2C
CRSF_FRAMETYPE_PARAMETER_WRITE = 0x2D
CRSF_FRAMETYPE_COMMAND = 0x32
CRSF_FRAMETYPE_RADIO_ID = 0x3A
CRSF_FRAMETYPE_MSP_REQ = 0x7A           # response request using msp sequence as command
CRSF_FRAMETYPE_MSP_RESP = 0x7B          # reply with 58 byte chunked binary
CRSF_FRAMETYPE_MSP_WRITE = 0x7C         # write with 8 byte chunked binary (OpenTX outbound telemetry buffer limit)
CRSF_FRAMETYPE_DISPLAYPORT_CMD = 0x7D   # displayport control command

def CRSF_FRAMETYPE_2_NAME(id):
    type_2_name = {
        CRSF_FRAMETYPE_GPS: "GPS",
        CRSF_FRAMETYPE_BATTERY_SENSOR: "BATTERY",
        CRSF_FRAMETYPE_LINK_STATISTICS: "LINK_STAT",
        CRSF_FRAMETYPE_LINK_STATISTICS_ELRS: "LINK_STAT_ELRS",
        CRSF_FRAMETYPE_RC_CHANNELS_PACKED: "RC DATA v2",
        CRSF_FRAMETYPE_SUBSET_RC_CHANNELS_PACKED: "RC DATA v3",
        CRSF_FRAMETYPE_LINK_STATISTICS_RX: "LINK STAT RX",
        CRSF_FRAMETYPE_LINK_STATISTICS_TX: "LINK STAT TX",
        CRSF_FRAMETYPE_ATTITUDE: "ATTITUDE",
        CRSF_FRAMETYPE_FLIGHT_MODE: "FLIGHT_MODE",
        CRSF_FRAMETYPE_DEVICE_PING: "PING",
        CRSF_FRAMETYPE_DEVICE_INFO: "INFO",
        CRSF_FRAMETYPE_PARAMETER_SETTINGS_ENTRY: "PARAM_SETTING_ENTRY",
        CRSF_FRAMETYPE_PARAMETER_READ: "PARAM READ",
        CRSF_FRAMETYPE_PARAMETER_WRITE: "PARAM WRITE",
        CRSF_FRAMETYPE_COMMAND: "COMMAND",
        CRSF_FRAMETYPE_RADIO_ID: "RADIO_ ID",
        CRSF_FRAMETYPE_MSP_REQ: "MSP REQ",
        CRSF_FRAMETYPE_MSP_RESP: "MSP RESP",
        CRSF_FRAMETYPE_MSP_WRITE: "MSP WRITE",
        CRSF_FRAMETYPE_DISPLAYPORT_CMD: "DISPLAYPORT CMD",
    }
    return type_2_name.get(id, "UNKNOWN")


CRSF_RADIO_ID_SUBTYPE_TIMING_SYNC = 0x10
def CRSF_RadioID_Subtype_2_Name(id):
    params = {
        CRSF_RADIO_ID_SUBTYPE_TIMING_SYNC: "TIMING SYNC",
    }
    return params.get(id, "??")


CRSF_DISPLAYPORT_SUBCMD_UPDATE = 0x01
CRSF_DISPLAYPORT_SUBCMD_CLEAR = 0X02
CRSF_DISPLAYPORT_SUBCMD_OPEN = 0x03
CRSF_DISPLAYPORT_SUBCMD_CLOSE = 0x04
CRSF_DISPLAYPORT_SUBCMD_POLL = 0x05

def CRSF_Displayport_Subcmd_2_Name(id):
    params = {
        CRSF_DISPLAYPORT_SUBCMD_UPDATE: "UPDATE",
        CRSF_DISPLAYPORT_SUBCMD_CLEAR: "CLEAR",
        CRSF_DISPLAYPORT_SUBCMD_OPEN: "OPEN",
        CRSF_DISPLAYPORT_SUBCMD_CLOSE: "CLOSE",
        CRSF_DISPLAYPORT_SUBCMD_POLL: "POLL",
    }
    return params.get(id, "??")


CRSF_ADDRESS_BROADCAST = 0x00
CRSF_ADDRESS_USB = 0x10
CRSF_ADDRESS_TBS_CORE_PNP_PRO = 0x80
CRSF_ADDRESS_RESERVED1 = 0x8A
CRSF_ADDRESS_CURRENT_SENSOR = 0xC0
CRSF_ADDRESS_GPS = 0xC2
CRSF_ADDRESS_TBS_BLACKBOX = 0xC4
CRSF_ADDRESS_FLIGHT_CONTROLLER = 0xC8
CRSF_ADDRESS_RESERVED2 = 0xCA
CRSF_ADDRESS_RACE_TAG = 0xCC
CRSF_ADDRESS_RADIO_TRANSMITTER = 0xEA
CRSF_ADDRESS_CRSF_RECEIVER = 0xEC
CRSF_ADDRESS_CRSF_TRANSMITTER = 0xEE

def CRSF_ADDR_2_NAME(addr):
    addr_2_name = {
        CRSF_ADDRESS_BROADCAST: "BROADCAST",
        CRSF_ADDRESS_USB: "USB",
        CRSF_ADDRESS_TBS_CORE_PNP_PRO: "TBS CORE PNP PRO",
        CRSF_ADDRESS_RESERVED1: "RESERVED1",
        CRSF_ADDRESS_CURRENT_SENSOR: "CURRENT SENSOR",
        CRSF_ADDRESS_GPS: "GPS",
        CRSF_ADDRESS_TBS_BLACKBOX: "TBS BLACKBOX",
        CRSF_ADDRESS_FLIGHT_CONTROLLER: "FLIGHT CONTROLLER",
        CRSF_ADDRESS_RESERVED2: "RESERVED2",
        CRSF_ADDRESS_RACE_TAG: "RACE TAG",
        CRSF_ADDRESS_RADIO_TRANSMITTER: "RADIO TRANSMITTER",
        CRSF_ADDRESS_CRSF_RECEIVER: "CRSF RX",
        CRSF_ADDRESS_CRSF_TRANSMITTER: "CRSF TX",
    }
    return addr_2_name.get(addr, "UNKNOWN")

CRSF_COMMAND_SUBCMD_GENERAL = 0x0A    # general command
CRSF_COMMAND_SUBCMD_GENERAL_CRSF_SPEED_PROPOSAL = 0x70    # proposed new CRSF port speed
CRSF_COMMAND_SUBCMD_GENERAL_CRSF_SPEED_RESPONSE = 0x71    # response to the proposed CRSF port speed

def CRSF_SUBCMD_2_NAME(cmd):
    cmd_2_name = {
        CRSF_COMMAND_SUBCMD_GENERAL: "GENERAL",
        CRSF_COMMAND_SUBCMD_GENERAL_CRSF_SPEED_PROPOSAL: "SPEED_PROPOSAL",
        CRSF_COMMAND_SUBCMD_GENERAL_CRSF_SPEED_RESPONSE: "SPEED_RESPONSE",
    }
    return cmd_2_name.get(cmd, "UNKNOWN")