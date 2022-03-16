from typing import Any

MSP_CRC_POLY = 0xD5

MSP_START = ord('$')

MSP_VERSION_V1 = ord('M')
MSP_VERSION_V2 = ord('X')
MSP_VERSION = {
    MSP_VERSION_V1: "MSPv1",
    MSP_VERSION_V2: "MSPv2",
}

MSP_TYPE_REQ = ord('<')
MSP_TYPE_RESP = ord('>')
MSP_TYPE_ERROR = ord('!')
MSP_TYPE_ELRS = ord('?')  # custom type
MSP_TYPE = {
    MSP_TYPE_REQ: "REQ",
    MSP_TYPE_RESP: "RESP",
    MSP_TYPE_ERROR: "ERROR",
}


# ----------------------------------------------
#                   MSP v1
# ----------------------------------------------

MSPv1_FUNC_TO_NAME = {
    1: "MSP_API_VERSION",
    2: "MSP_FC_VARIANT",
    3: "MSP_FC_VERSION",
    4: "MSP_BOARD_INFO",
    5: "MSP_BUILD_INFO",

    10: "MSP_NAME",
    11: "MSP_SET_NAME",

    32: "MSP_BATTERY_CONFIG",
    33: "MSP_SET_BATTERY_CONFIG",

    34: "MSP_MODE_RANGES",
    35: "MSP_SET_MODE_RANGE",

    36: "MSP_FEATURE_CONFIG",
    37: "MSP_SET_FEATURE_CONFIG",

    38: "MSP_BOARD_ALIGNMENT_CONFIG",
    39: "MSP_SET_BOARD_ALIGNMENT_CONFIG",

    40: "MSP_CURRENT_METER_CONFIG",
    41: "MSP_SET_CURRENT_METER_CONFIG",

    42: "MSP_MIXER_CONFIG",
    43: "MSP_SET_MIXER_CONFIG",

    44: "MSP_RX_CONFIG",
    45: "MSP_SET_RX_CONFIG",

    46: "MSP_LED_COLORS",
    47: "MSP_SET_LED_COLORS",

    48: "MSP_LED_STRIP_CONFIG",
    49: "MSP_SET_LED_STRIP_CONFIG",

    50: "MSP_RSSI_CONFIG",
    51: "MSP_SET_RSSI_CONFIG",

    52: "MSP_ADJUSTMENT_RANGES",
    53: "MSP_SET_ADJUSTMENT_RANGE",

    54: "MSP_CF_SERIAL_CONFIG",
    55: "MSP_SET_CF_SERIAL_CONFIG",

    56: "MSP_VOLTAGE_METER_CONFIG",
    57: "MSP_SET_VOLTAGE_METER_CONFIG",

    58: "MSP_SONAR_ALTITUDE",

    59: "MSP_PID_CONTROLLER",
    60: "MSP_SET_PID_CONTROLLER",

    61: "MSP_ARMING_CONFIG",
    62: "MSP_SET_ARMING_CONFIG",

    64: "MSP_RX_MAP",
    65: "MSP_SET_RX_MAP",

    66: "MSP_BF_CONFIG",
    67: "MSP_SET_BF_CONFIG",

    68: "MSP_REBOOT",

    69: "MSP_BF_BUILD_INFO",

    70: "MSP_DATAFLASH_SUMMARY",
    71: "MSP_DATAFLASH_READ",
    72: "MSP_DATAFLASH_ERASE",

    73: "MSP_LOOP_TIME",
    74: "MSP_SET_LOOP_TIME",

    75: "MSP_FAILSAFE_CONFIG",
    76: "MSP_SET_FAILSAFE_CONFIG",

    77: "MSP_RXFAIL_CONFIG",
    78: "MSP_SET_RXFAIL_CONFIG",

    79: "MSP_SDCARD_SUMMARY",

    80: "MSP_BLACKBOX_CONFIG",
    81: "MSP_SET_BLACKBOX_CONFIG",

    82: "MSP_TRANSPONDER_CONFIG",
    83: "MSP_SET_TRANSPONDER_CONFIG",

    84: "MSP_OSD_CONFIG",
    85: "MSP_SET_OSD_CONFIG",

    86: "MSP_OSD_CHAR_READ",
    87: "MSP_OSD_CHAR_WRITE",

    88: "MSP_VTX_CONFIG",
    89: "MSP_SET_VTX_CONFIG",

    90: "MSP_ADVANCED_CONFIG",
    91: "MSP_SET_ADVANCED_CONFIG",

    92: "MSP_FILTER_CONFIG",
    93: "MSP_SET_FILTER_CONFIG",

    94: "MSP_PID_ADVANCED",
    95: "MSP_SET_PID_ADVANCED",

    96: "MSP_SENSOR_CONFIG",
    97: "MSP_SET_SENSOR_CONFIG",

    98: "MSP_CAMERA_CONTROL",

    99: "MSP_SET_ARMING_DISABLED",

    180: "MSP_OSD_VIDEO_CONFIG",
    181: "MSP_SET_OSD_VIDEO_CONFIG",

    182: "MSP_DISPLAYPORT",

    183: "MSP_COPY_PROFILE",

    184: "MSP_BEEPER_CONFIG",
    185: "MSP_SET_BEEPER_CONFIG",

    186: "MSP_SET_TX_INFO",
    187: "MSP_TX_INFO",

    100: "MSP_IDENT",

    101: "MSP_STATUS",
    102: "MSP_RAW_IMU",
    103: "MSP_SERVO",
    104: "MSP_MOTOR",
    105: "MSP_RC",
    106: "MSP_RAW_GPS",
    107: "MSP_COMP_GPS",
    108: "MSP_ATTITUDE",
    109: "MSP_ALTITUDE",
    110: "MSP_ANALOG",
    111: "MSP_RC_TUNING",
    112: "MSP_PID",
    113: "MSP_BOX",
    114: "MSP_MISC",
    115: "MSP_MOTOR_PINS",
    116: "MSP_BOXNAMES",
    117: "MSP_PIDNAMES",
    118: "MSP_WP",
    119: "MSP_BOXIDS",
    120: "MSP_SERVO_CONFIGURATIONS",
    121: "MSP_NAV_STATUS",
    122: "MSP_NAV_CONFIG",

    124: "MSP_MOTOR_3D_CONFIG",
    125: "MSP_RC_DEADBAND",
    126: "MSP_SENSOR_ALIGNMENT",
    127: "MSP_LED_STRIP_MODECOLOR",
    128: "MSP_VOLTAGE_METERS",
    129: "MSP_CURRENT_METERS",
    130: "MSP_BATTERY_STATE",
    131: "MSP_MOTOR_CONFIG",
    132: "MSP_GPS_CONFIG",
    133: "MSP_COMPASS_CONFIG",
    134: "MSP_ESC_SENSOR_DATA",
    135: "MSP_GPS_RESCUE",
    136: "MSP_GPS_RESCUE_PIDS",
    137: "MSP_VTXTABLE_BAND",
    138: "MSP_VTXTABLE_POWERLEVEL",
    139: "MSP_MOTOR_TELEMETRY",

    140: "MSP_SIMPLIFIED_TUNING",
    141: "MSP_SET_SIMPLIFIED_TUNING",
    142: "MSP_CALCULATE_SIMPLIFIED_PID",
    143: "MSP_CALCULATE_SIMPLIFIED_GYRO",
    144: "MSP_CALCULATE_SIMPLIFIED_DTERM",
    145: "MSP_VALIDATE_SIMPLIFIED_TUNING",

    200: "MSP_SET_RAW_RC",
    201: "MSP_SET_RAW_GPS",
    202: "MSP_SET_PID",
    203: "MSP_SET_BOX",
    204: "MSP_SET_RC_TUNING",
    205: "MSP_ACC_CALIBRATION",
    206: "MSP_MAG_CALIBRATION",
    207: "MSP_SET_MISC",
    208: "MSP_RESET_CONF",
    209: "MSP_SET_WP",
    210: "MSP_SELECT_SETTING",
    211: "MSP_SET_HEADING",
    212: "MSP_SET_SERVO_CONFIGURATION",
    214: "MSP_SET_MOTOR",
    215: "MSP_SET_NAV_CONFIG",

    217: "MSP_SET_MOTOR_3D_CONFIG",
    218: "MSP_SET_RC_DEADBAND",
    219: "MSP_SET_RESET_CURR_PID",
    220: "MSP_SET_SENSOR_ALIGNMENT",
    221: "MSP_SET_LED_STRIP_MODECOLOR",
    222: "MSP_SET_MOTOR_CONFIG",
    223: "MSP_SET_GPS_CONFIG",
    224: "MSP_SET_COMPASS_CONFIG",
    225: "MSP_SET_GPS_RESCUE",
    226: "MSP_SET_GPS_RESCUE_PIDS",
    227: "MSP_SET_VTXTABLE_BAND",
    228: "MSP_SET_VTXTABLE_POWERLEVEL",

    240: "MSP_BIND",
    242: "MSP_ALARMS",

    250: "MSP_EEPROM_WRITE",

    251: "MSP_RESERVE_1",
    252: "MSP_RESERVE_2",
    253: "MSP_DEBUGMSG",
    254: "MSP_DEBUG",
    255: "MSP_V2_FRAME",

    # Additional commands that are not compatible with MultiWii
    150: "MSP_STATUS_EX",
    160: "MSP_UID",
    164: "MSP_GPSSVINFO",
    166: "MSP_GPSSTATISTICS",
    230: "MSP_MULTIPLE_MSP",
    238: "MSP_MODE_RANGES_EXTRA",
    240: "MSP_ACC_TRIM",
    239: "MSP_SET_ACC_TRIM",
    241: "MSP_SERVO_MIX_RULES",
    242: "MSP_SET_SERVO_MIX_RULE",
    245: "MSP_SET_PASSTHROUGH",
    246: "MSP_SET_RTC",
    247: "MSP_RTC",
    248: "MSP_SET_BOARD_INFO",
    249: "MSP_SET_SIGNATURE",
}


MSPv1_ELRS_FUNC_TO_NAME = {
    # Custom functions
    1: "ELRS_INT_MSP_PARAMS",
    100: "ELRS_HANDSET_BASE",
    101: "ELRS_HANDSET_CALIBRATE",
    102: "ELRS_HANDSET_MIXER",
    103: "ELRS_HANDSET_ADJUST",
    104: "ELRS_HANDSET_ADJUST_MIN",
    105: "ELRS_HANDSET_ADJUST_MID",
    106: "ELRS_HANDSET_ADJUST_MAX",
    107: "ELRS_HANDSET_CONFIGS_LOAD",
    108: "ELRS_HANDSET_CONFIGS_SAVE",
    109: "ELRS_HANDSET_TLM_LINK_STATS",
    110: "ELRS_HANDSET_TLM_BATTERY",
    111: "ELRS_HANDSET_TLM_GPS",
}

def MSPv1_function_get(id, type=None):
    if type == MSP_TYPE_ELRS:
        return MSPv1_ELRS_FUNC_TO_NAME.get(id, f"0x{id:02X} ??")
    return MSPv1_FUNC_TO_NAME.get(id, f"0x{id:02X} ??")

class StoreVal:
    def __init__(self, value = None) -> None:
        self.__val = value
    @property
    def value(self) -> Any:
        if self.__val is None:
            raise ValueError("Value not set!")
        return self.__val
    @value.setter
    def value(self, val):
        self.__val = val


MSPv1_MSG_CONTENT = {
    1: [ # MSP_API_VERSION
        (1, "Protocol Ver"),
        (1, "Major"),
        (1, "Minor"),
    ],
    2: [ # MSP_FC_VARIANT
        (-1, str),
    ],
    3: [ # MSP_FC_VERSION
        (1, "Major"),
        (1, "Minor"),
        (1, "Patch"),
    ],
    5: [ # MSP_BUILD_INFO
        (11, str, "data: "),
        (8, str, "time: "),
        (7, str, "SHA: "),
    ],
    10: [ # MSP_NAME
        (-1, str, "Name: "),
    ],
    11: [ # MSP_SET_NAME
        (-1, str, "Name: "),
    ],
    46: [ # MSP_LED_COLORS
        (2, "H: {}"),
        (1, "S: {}"),
        (1, "V: {}"),
    ] * 16,
    47: [ # MSP_SET_LED_COLORS
        (2, "H: {}"),
        (1, "S: {}"),
        (1, "V: {}"),
    ] * 16,
    48:   # MSP_LED_STRIP_CONFIG
        [ (4, "Config: {:#X}") ] * 32 +
        [
            (1, "Advanced: {}"),
            (1, "Profile: {}"),
        ]
    ,
    49: [ # MSP_SET_LED_STRIP_CONFIG
        (1, "Index: {}"),
        (4, "Config: {:#X}"),
        (1, "Profile: {}"),
    ],
    88: [ # MSP_VTX_CONFIG
        (1, {0:"VTXDEV_UNSUPPORTED", 1:"VTXDEV_RTC6705", 2:"VTXDEV_SMARTAUDIO", 3:"VTXDEV_TRAMP", 4:"VTXDEV_UNKNOWN"}),
        (1, "Band"),
        (1, "Channel"),
        (1, "Power"),
        (1, "Pit Mode"),
        (2, "Freq {}"),
        (1, "Ready"),
        (1, "Low Power Disarm"),
        (2, "Pit Mode Freq: {}"),
        (1, "VTX Table Available"),
        (1, "Bands Count"),
        (1, "Channels Count"),
        (1, "Power Levels Count"),
    ],
    89: [ # MSP_SET_VTX_CONFIG
        (2, "Freq: {}"),
        (1, "Power: {}"),
        (1, "Pit Mode: {}"),
        (1, "Low Power Disarm"),
        (2, "Pit Mode Freq: {}"),
        (1, "New Band: {}"),
        (1, "New Channel: {}"),
        (2, "New Freq: {}"),
        (1, "Bands Count: {}"),
        (1, "Channels Count: {}"),
        (1, "Power Levels Count: {}"),
        (1, "Clear VTX Table: {}"),
    ],
    101: [ # MSP_STATUS
        (2, "PID us: {}"),
        (2, "I2C errors: {}"),
        (2, "Sensors mask: {:#X}"),
        (4, "Flight Mode Flags: {:#X}"),
        (1, "PID Profile Idx"),
        (2, "System Load Avg: {}"),
        (2, "Gyro Cycle Time: {}"),
        (1, "Flight Mode Cnt"),
        (0, "Flight Mode {:#X}", StoreVal),
        (1, "Arming Disabled Flags Count"),
        (4, "Arming Disabled Flags: {:#X}"),
        (1, "Config State Flags"),
    ],
    150: [ # MSP_STATUS_EX
        (2, "PID us: {}"),
        (2, "I2C errors: {}"),
        (2, "Sensors mask: {:#X}"),
        (4, "Flight Mode Flags: {:#X}"),
        (1, "PID Profile Idx"),
        (2, "System Load Avg: {}"),
        (1, "PID Profile Count: {}"),
        (1, "Rate Profile Idx: {}"),
        (1, "Flight Mode Cnt"),
        (0, "Flight Mode {:#X}", StoreVal),
        (1, "Arming Disabled Flags Count"),
        (4, "Arming Disabled Flags: {:#X}"),
        (1, "Config State Flags"),
    ],
    105:  # MSP_RC
        [(2, f"CH{x} {{:d}}") for x in range(18)]
    ,
    182: [ # MSP_DISPLAYPORT
        (1, {0:"Heartbeat", 1:"release", 2:"clear", 3:"write", 4:"draw"}),
        (1, "row"),
        (1, "col"),
        (1, "attr"),
        (-1, str, "Value: "),
    ],
}

MSPv1_ELRS_MSG_CONTENT = {
    # Custom functions
    1: [  # ELRS_INT_MSP_PARAMS
        (1, "rate"),
        (1, "tlm"),
        (1, "pwr, current"),
        (1, "pwr, max"),
        (1, "rf mode"),
        (-1, str),  # sha
    ],
    102:  # ELRS_HANDSET_MIXER
        [ (1, "mixer index"), (1, "index"), (1, "inverted"), (1, "scale"), ] * 4 +
        [ (1, "mixer index"), (1, "index"), (1, "inverted") ] * 8
    ,
    104: [  # ELRS_HANDSET_ADJUST_MIN
        (1, "index"),
        (2, "value"),
    ],
    105: [  # ELRS_HANDSET_ADJUST_MID
        (1, "index"),
        (2, "value"),
    ],
    106: [  # ELRS_HANDSET_ADJUST_MAX
        (1, "index"),
        (2, "value"),
    ],
    109: [  # ELRS_HANDSET_TLM_LINK_STATS
        (1, "UL RSSI 1: {}"),
        (1, "UL RSSI 2: {}"),
        (1, "UL LQ: {}"),
        (1, "UL SNR: {:d}"),
        (1, "active antenna: {}"),
        (1, "RF Mode: {}"),
        (1, "UL TX Power: {}"),
        (1, "DL RSSI: {}"),
        (1, "DL LQ: {}"),
        (1, "DL SNR: {:d}"),
    ],
    110: [  # ELRS_HANDSET_TLM_BATTERY
        (2, "Voltage {}"),
        (2, "Current {}"),
        (1, "Remaining: {}"),
        (3, "Capacity: {}"),
    ],
    111: [  # ELRS_HANDSET_TLM_GPS
        (4, "latitude: {:d}"),
        (4, "longitude: {:d}"),
        (2, "speed"),
        (2, "heading"),
        (2, "altitude"),
        (1, "satellites"),
        (1, "pkt_cnt"),
    ],
}

def MSPv1_function_content_get(func, type=None):
    if type == MSP_TYPE_ELRS:
        return MSPv1_ELRS_MSG_CONTENT.get(id, [])
    return MSPv1_MSG_CONTENT.get(func, [])


# ----------------------------------------------
#                   MSP v2
# ----------------------------------------------

MSPv2_FUNC_TO_NAME = {

    # ----------------------------------------------
    # ExpressLRS Backpack Protocol Specification v1.1
    0x0300: "GET BAND/CHANNEL INDEX",
    0x0301: "SET BAND/CHANNEL INDEX",
    0x0302: "GET FREQ",
    0x0303: "SET FREQ",
    0x0304: "GET RECORDING STATE",
    0x0305: "SET RECORDING STATE",
    0x0306: "GET VRX MODE",
    0x0307: "SET VRX MODE",
    0x0308: "GET RSSI",
    0x0309: "GET BATTERY VOLTAGE",
    0x030A: "GET FIRMWARE",
    0x030B: "SET BUZZER",
    0x030C: "SET OSD ELEMENT",
    # ----------------------------------------------
}

def MSPv2_function_get(id):
    if id < 255:
        return MSPv1_function_get(id)
    return MSPv2_FUNC_TO_NAME.get(id, f"0x{id:04X} ??")


MSPv2_MSG_CONTENT = {

    # ----------------------------------------------
    # ExpressLRS Backpack Protocol Specification v1.1

    0x0300: [ # "GET BAND/CHANNEL INDEX",
        (1, "Index: {}"),
    ],
    0x0301: [ # "SET BAND/CHANNEL INDEX",
        (1, "Index: {}"),
    ],
    0x0302: [ # "GET FREQ",
        (2, "Freq: {}MHz"),
    ],
    0x0303: [ # "SET FREQ",
        (2, "Freq: {}MHz"),
    ],
    0x0304: [ # "GET RECORDING STATE",
        (1, {0:"OFF", 1:"ON"}, "Recording: "),
    ],
    0x0305: [ # "SET RECORDING STATE",
        (1, {0:"STOP", 1:"START"}, "Recording: "),
        (2, "Delay: {}s"),
    ],
    0x0306: [ # "GET VRX MODE",
        (1, "Mode: {}"),
    ],
    0x0307: [ # "SET VRX MODE",
        (1, "Mode: {}"),
    ],
    0x0308:  # "GET RSSI",
        [ (1, "Num Antennas: {}") ] + [ (1, "RSSI: -{}") ] * 16
    ,
    0x0309: [ # "GET BATTERY VOLTAGE",
        (2, "Volate: {}mV"),
    ],
    0x030A: [ # "GET FIRMWARE",
        (1, "Size: {}"),
        (-1, None, "fw field: "),
    ],
    0x030B: [ # "SET BUZZER",
        (2, "Duration: {}ms"),
    ],
    # ----------------------------------------------
}

def MSPv2_function_content_get(func):
    if func < 255:
        return MSPv1_function_content_get(func)
    return MSPv2_MSG_CONTENT.get(func, [])
