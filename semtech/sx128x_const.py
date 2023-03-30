
#*****************************************************************
#  SX128x GENERIC
#*****************************************************************
SX128X_XTAL_FREQ                   = 52000000.0
SX128X_FREQ_STEP                   = (SX128X_XTAL_FREQ / (0x1 << 18))
SX128X_SPI_REG_READ                = 0x00
SX128X_SPI_REG_WRITE               = 0x00
SX128X_SPI_REG_MASK                = 0xFF

def SX128x_XO_Freq_set(freq):
    global SX128X_XTAL_FREQ
    global SX128X_FREQ_STEP
    SX128X_XTAL_FREQ = freq
    SX128X_FREQ_STEP = freq / (1 << 18)
    print(f"XO Freq set to {freq}")



#*****************************************************************
#  SX128x COMMANDS
#*****************************************************************
SX1280_RADIO_GET_PACKETTYPE = 0x03
SX1280_RADIO_GET_IRQSTATUS = 0x15
SX1280_RADIO_GET_RXBUFFERSTATUS = 0x17
SX1280_RADIO_WRITE_REGISTER = 0x18
SX1280_RADIO_READ_REGISTER = 0x19
SX1280_RADIO_WRITE_BUFFER = 0x1A
SX1280_RADIO_READ_BUFFER = 0x1B
SX1280_RADIO_GET_PACKETSTATUS = 0x1D
SX1280_RADIO_GET_RSSIINST = 0x1F
SX1280_RADIO_SET_STANDBY = 0x80
SX1280_RADIO_SET_RX = 0x82
SX1280_RADIO_SET_TX = 0x83
SX1280_RADIO_SET_SLEEP = 0x84
SX1280_RADIO_SET_RFFREQUENCY = 0x86
SX1280_RADIO_SET_CADPARAMS = 0x88
SX1280_RADIO_CALIBRATE = 0x89
SX1280_RADIO_SET_PACKETTYPE = 0x8A
SX1280_RADIO_SET_MODULATIONPARAMS = 0x8B
SX1280_RADIO_SET_PACKETPARAMS = 0x8C
SX1280_RADIO_SET_DIOIRQPARAMS = 0x8D
SX1280_RADIO_SET_TXPARAMS = 0x8E
SX1280_RADIO_SET_BUFFERBASEADDRESS = 0x8F
SX1280_RADIO_SET_RXDUTYCYCLE = 0x94
SX1280_RADIO_SET_REGULATORMODE = 0x96
SX1280_RADIO_CLR_IRQSTATUS = 0x97
SX1280_RADIO_SET_AUTOTX = 0x98
SX1280_RADIO_SET_LONGPREAMBLE = 0x9B
SX1280_RADIO_SET_PERF_COUNTER_MODE = 0x9C
SX1280_RADIO_SET_UARTSPEED = 0x9D
SX1280_RADIO_SET_AUTOFS = 0x9E
SX1280_RADIO_SET_RANGING_ROLE = 0xA3
SX1280_RADIO_GET_STATUS = 0xC0
SX1280_RADIO_SET_FS = 0xC1
SX1280_RADIO_SET_CAD = 0xC5
SX1280_RADIO_SET_TXCONTINUOUSWAVE = 0xD1
SX1280_RADIO_SET_TXCONTINUOUSPREAMBLE = 0xD2
SX1280_RADIO_SET_SAVECONTEXT = 0xD5

SX128X_COMMAND_READ = [
    SX1280_RADIO_GET_PACKETTYPE,
    SX1280_RADIO_GET_IRQSTATUS,
    SX1280_RADIO_GET_RXBUFFERSTATUS,
    SX1280_RADIO_READ_REGISTER,
    SX1280_RADIO_READ_BUFFER,
    SX1280_RADIO_GET_PACKETSTATUS,
    SX1280_RADIO_GET_RSSIINST,
    SX1280_RADIO_GET_STATUS,
]

SX128X_COMMAND_NAMES = {
    SX1280_RADIO_GET_PACKETTYPE: "GET_PACKETTYPE",
    SX1280_RADIO_GET_IRQSTATUS: "GET_IRQSTATUS",
    SX1280_RADIO_GET_RXBUFFERSTATUS: "GET_RXBUFFERSTATUS",
    SX1280_RADIO_WRITE_REGISTER: "WRITE_REGISTER",
    SX1280_RADIO_READ_REGISTER: "READ_REGISTER",
    SX1280_RADIO_WRITE_BUFFER: "WRITE_BUFFER",
    SX1280_RADIO_READ_BUFFER: "READ_BUFFER",
    SX1280_RADIO_GET_PACKETSTATUS: "GET_PACKETSTATUS",
    SX1280_RADIO_GET_RSSIINST: "GET_RSSIINST",
    SX1280_RADIO_SET_STANDBY: "SET_STANDBY",
    SX1280_RADIO_SET_RX: "SET_RX",
    SX1280_RADIO_SET_TX: "SET_TX",
    SX1280_RADIO_SET_SLEEP: "SET_SLEEP",
    SX1280_RADIO_SET_RFFREQUENCY: "SET_RFFREQUENCY",
    SX1280_RADIO_SET_CADPARAMS: "SET_CADPARAMS",
    SX1280_RADIO_CALIBRATE: "CALIBRATE",
    SX1280_RADIO_SET_PACKETTYPE: "SET_PACKETTYPE",
    SX1280_RADIO_SET_MODULATIONPARAMS: "SET_MODULATIONPARAMS",
    SX1280_RADIO_SET_PACKETPARAMS: "SET_PACKETPARAMS",
    SX1280_RADIO_SET_DIOIRQPARAMS: "SET_DIOIRQPARAMS",
    SX1280_RADIO_SET_TXPARAMS: "SET_TXPARAMS",
    SX1280_RADIO_SET_BUFFERBASEADDRESS: "SET_BUFFERBASEADDRESS",
    SX1280_RADIO_SET_RXDUTYCYCLE: "SET_RXDUTYCYCLE",
    SX1280_RADIO_SET_REGULATORMODE: "SET_REGULATORMODE",
    SX1280_RADIO_CLR_IRQSTATUS: "CLR_IRQSTATUS",
    SX1280_RADIO_SET_AUTOTX: "SET_AUTOTX",
    SX1280_RADIO_SET_LONGPREAMBLE: "SET_LONGPREAMBLE",
    SX1280_RADIO_SET_PERF_COUNTER_MODE: "PERF_COUNTER_MODE",
    SX1280_RADIO_SET_UARTSPEED: "SET_UARTSPEED",
    SX1280_RADIO_SET_AUTOFS: "SET_AUTOFS",
    SX1280_RADIO_SET_RANGING_ROLE: "SET_RANGING_ROLE",
    SX1280_RADIO_GET_STATUS: "GET_STATUS",
    SX1280_RADIO_SET_FS: "SET_FS",
    SX1280_RADIO_SET_CAD: "SET_CAD",
    SX1280_RADIO_SET_TXCONTINUOUSWAVE: "SET_TXCONTINUOUSWAVE",
    SX1280_RADIO_SET_TXCONTINUOUSPREAMBLE: "SET_TXCONTINUOUSPREAMBLE",
    SX1280_RADIO_SET_SAVECONTEXT: "SET_SAVECONTEXT",
}

def SX128x_Command_Name_get(cmd):
    # remove MSB which is register write flag
    return cmd in SX128X_COMMAND_READ, SX128X_COMMAND_NAMES.get(cmd, "")



#*****************************************************************
#  SX128x REGISTERS
#*****************************************************************
SX1280_REG_LR_FIRMWARE_VERSION_MSB  = 0x0153
SX1280_REG_LR_FIRMWARE_VERSION_LSB  = 0x0154
SX1280_REG_SENSITIVITY              = 0x0891
SX1280_REG_LORA_SYNCWORD_MSB        = 0x0944
SX1280_REG_LR_ESTIMATED_FREQUENCY_ERROR_MSB = 0x0954

SX1280_REG_RANGING_REQ_ADDR_1_MASTER = 0x912
SX1280_REG_RANGING_REQ_ADDR_2_MASTER = 0x913
SX1280_REG_RANGING_REQ_ADDR_3_MASTER = 0x914
SX1280_REG_RANGING_REQ_ADDR_4_MASTER = 0x915
SX1280_REG_RANGING_REQ_ADDR_1_SLAVE  = 0x916
SX1280_REG_RANGING_REQ_ADDR_2_SLAVE  = 0x917
SX1280_REG_RANGING_REQ_ADDR_3_SLAVE  = 0x918
SX1280_REG_RANGING_REQ_ADDR_4_SLAVE  = 0x919
SX1280_REG_RANGING_REQ_ADDR_BITS     = 0x931
SX1280_REG_RANGING_CALIB_MSB         = 0x92C
SX1280_REG_RANGING_CALIB_LSB         = 0x92D
SX1280_REG_RANGING_RESULT_MSB        = 0x961
SX1280_REG_RANGING_RESULT_MID        = 0x962
SX1280_REG_RANGING_RESULT_LSB        = 0x963

SX1280_REG_CRC_POLY_MSB = 0x9c6
SX1280_REG_CRC_POLY_LSB = 0x9c7 # Check for BLE (= CRC SEED MSB)!
SX1280_REG_CRC_SEED_MSB = 0x9c8
SX1280_REG_CRC_SEED_LSB = 0x9c9
SX1280_REG_SYNCWORD1_0  = 0x9CE
SX1280_REG_SYNCWORD1_1  = 0x9CF
SX1280_REG_SYNCWORD1_2  = 0x9D0
SX1280_REG_SYNCWORD1_3  = 0x9D1
SX1280_REG_SYNCWORD1_4  = 0x9D2
SX1280_REG_SYNCWORD2_0  = 0x9D3
SX1280_REG_SYNCWORD2_1  = 0x9D4
SX1280_REG_SYNCWORD2_2  = 0x9D5
SX1280_REG_SYNCWORD2_3  = 0x9D6
SX1280_REG_SYNCWORD2_4  = 0x9D7
SX1280_REG_SYNCWORD3_0  = 0x9D8
SX1280_REG_SYNCWORD3_1  = 0x9D9
SX1280_REG_SYNCWORD3_2  = 0x9DA
SX1280_REG_SYNCWORD3_3  = 0x9DB
SX1280_REG_SYNCWORD3_4  = 0x9DC

SX1280_REG_TO_NAME = {
    SX1280_REG_LR_FIRMWARE_VERSION_MSB: "FW VERSION (MSB)",
    SX1280_REG_LR_FIRMWARE_VERSION_LSB: "FW VERSION (LSB)",
    SX1280_REG_SENSITIVITY: "SENSITIVITY",
    SX1280_REG_LORA_SYNCWORD_MSB: "LORA SYNC WORD",
    SX1280_REG_LR_ESTIMATED_FREQUENCY_ERROR_MSB: "FREQ ERROR",

    SX1280_REG_RANGING_REQ_ADDR_1_MASTER: "RAGING Addr Master 1",
    SX1280_REG_RANGING_REQ_ADDR_2_MASTER: "RAGING Addr Master 2",
    SX1280_REG_RANGING_REQ_ADDR_3_MASTER: "RAGING Addr Master 3",
    SX1280_REG_RANGING_REQ_ADDR_4_MASTER: "RAGING Addr Master 4",
    SX1280_REG_RANGING_REQ_ADDR_1_SLAVE: "RAGING Addr Slave 1",
    SX1280_REG_RANGING_REQ_ADDR_2_SLAVE: "RAGING Addr Slave 2",
    SX1280_REG_RANGING_REQ_ADDR_3_SLAVE: "RAGING Addr Slave 3",
    SX1280_REG_RANGING_REQ_ADDR_4_SLAVE: "RAGING Addr Slave 4",
    SX1280_REG_RANGING_REQ_ADDR_BITS: "RAGING Addr Bits",
    SX1280_REG_RANGING_CALIB_MSB: "RAGING Calibration, MSB",
    SX1280_REG_RANGING_CALIB_LSB: "RAGING Calibration, LSB",
    SX1280_REG_RANGING_RESULT_MSB: "RAGING RES MSB",
    SX1280_REG_RANGING_RESULT_MID: "RAGING RES MID",
    SX1280_REG_RANGING_RESULT_LSB: "RAGING RES LSB",

    SX1280_REG_CRC_POLY_MSB: "CRC POLY MSB",
    SX1280_REG_CRC_POLY_LSB: "CRC POLY LSB",
    SX1280_REG_CRC_SEED_MSB: "CRC SEED MSB",
    SX1280_REG_CRC_SEED_LSB: "CRC SEED LSB",
    SX1280_REG_SYNCWORD1_0: "SYNCWORD1.0",
    SX1280_REG_SYNCWORD1_1: "SYNCWORD1.1",
    SX1280_REG_SYNCWORD1_2: "SYNCWORD1.2",
    SX1280_REG_SYNCWORD1_3: "SYNCWORD1.3",
    SX1280_REG_SYNCWORD1_4: "SYNCWORD1.4",
    SX1280_REG_SYNCWORD2_0: "SYNCWORD2.0",
    SX1280_REG_SYNCWORD2_1: "SYNCWORD2.1",
    SX1280_REG_SYNCWORD2_2: "SYNCWORD2.2",
    SX1280_REG_SYNCWORD2_3: "SYNCWORD2.3",
    SX1280_REG_SYNCWORD2_4: "SYNCWORD2.4",
    SX1280_REG_SYNCWORD3_0: "SYNCWORD3.0",
    SX1280_REG_SYNCWORD3_1: "SYNCWORD3.1",
    SX1280_REG_SYNCWORD3_2: "SYNCWORD3.2",
    SX1280_REG_SYNCWORD3_3: "SYNCWORD3.3",
    SX1280_REG_SYNCWORD3_4: "SYNCWORD3.4",
}

def SX128x_Register_Name_get(reg, default="Register"):
    return SX1280_REG_TO_NAME.get(reg, default)



#*****************************************************************
#  SX128x REGISTER SETTINGS
#*****************************************************************
SX128x_PKT_TYPE_GFSK = 0
SX128x_PKT_TYPE_LORA = 1
SX128x_PKT_TYPE_RANGING = 2
SX128x_PKT_TYPE_FLRC = 3
SX128x_PKT_TYPE_BLE = 4
SX128x_PKT_TYPE_INVALID = None
SX128x_PKT_TYPE_NAME = {
    SX128x_PKT_TYPE_GFSK: "GFSK",
    SX128x_PKT_TYPE_LORA: "LORA",
    SX128x_PKT_TYPE_RANGING: "RANGING",
    SX128x_PKT_TYPE_FLRC: "FLRC",
    SX128x_PKT_TYPE_BLE: "BLE",
}
def SX128x_Pkt_Type_get(value):
    return SX128x_PKT_TYPE_NAME.get(value, SX128x_PKT_TYPE_INVALID)


STATUS_CONFIG = [
    (7, 5, ["Reserved", "Reserved", "STDBY_RC", "STDBY_XOSC", "FS", "Rx", "Tx", "Reserved"]),
    (4, 2, ["Reserved", "Transceiver OK", "Data Available", "Cmd Timeout",
            "Cmd Error", "Cmd Exec Fail", "Cmd Tx Done", "Reserved"]),
    (1, 1, ["Reserved", "Reserved"]),
    (0, 0, ["IDLE", "BUSY"]),
]
DIOIRQ_CONFIG = [
    (15, 15, ["", "PreambleDetected"]),
    (14, 14, ["", "RxTxTimeout"]),
    (13, 13, ["", "CadDetected"]),
    (12, 12, ["", "CadDone"]),
    (11, 11, ["", "RangingMasterRequestValid"]),
    (10, 10, ["", "RangingMasterTimeout"]),
    ( 9,  9, ["", "RangingMasterResultValid"]),
    ( 8,  8, ["", "RangingSlaveRequestDiscard"]),
    ( 7,  7, ["", "RangingSlaveResponseDone"]),
    ( 6,  6, ["", "CrcError"]),
    ( 5,  5, ["", "HeaderError"]),
    ( 4,  4, ["", "HeaderValid"]),
    ( 3,  3, ["", "SyncWordError"]),
    ( 2,  2, ["", "SyncWordValid"]),
    ( 1,  1, ["", "RxDone"]),
    ( 0,  0, ["", "TxDone"]),
]
PACKET_TYPE_CONFIG = [
    (7, 0, {"name": "Type", "values": SX128x_PKT_TYPE_NAME})
]

GFSK_BLE_BR_CONFIG = {
    0x04: "BR_2_000_BW_2_4",
    0x28: "BR_1_600_BW_2_4",
    0x4C: "BR_1_000_BW_2_4",
    0x45: "BR_1_000_BW_1_2",
    0x70: "BR_0_800_BW_2_4",
    0x69: "BR_0_800_BW_1_2",
    0x8D: "BR_0_500_BW_1_2",
    0x86: "BR_0_500_BW_0_6",
    0xB1: "BR_0_400_BW_1_2",
    0xAA: "BR_0_400_BW_0_6",
    0xCE: "BR_0_250_BW_0_6",
    0xC7: "BR_0_250_BW_0_3",
}
GFSK_BLE_MOD_CONFIG = {x:f"Modindex: {.25*(x+1)}" for x in range(16)}
GFSK_BLE_FLRC_BT_CONFIG = {
    0x00: "OFF",
    0x10: "1",
    0x20: "0.5",
}

FLRC_BR_CONFIG = {
    0x45: "BR_1_300_BW_1_2",
    0x69: "BR_1_000_BW_1_2",
    0x86: "BR_0_650_BW_0_6",
    0xAA: "BR_0_520_BW_0_6",
    0xC7: "BR_0_325_BW_0_3",
    0xEB: "BR_0_260_BW_0_3",
}
FLRC_CR_CONFIG = {
    0x0: "CR_1_2",
    0x2: "CR_3_4",
    0x4: "CR_1_0",
}

LORA_SF_CONFIG = {
    0x50: 'SF 5',
    0x60: 'SF 6',
    0x70: 'SF 7',
    0x80: 'SF 8',
    0x90: 'SF 9',
    0xa0: 'SF 10',
    0xb0: 'SF 11',
    0xc0: 'SF 12',
}
LORA_BW_CONFIG = {
    0x0A: "BW 1625",
    0x18: "BW 812.5",
    0x26: "BW 406.25",
    0x34: "BW 203.125",
}
LORA_CR_CONFIG = {
    0x01: "CR_4_5",
    0x02: "CR_4_6",
    0x03: "CR_4_7",
    0x04: "CR_4_8",
    0x05: "CR_LI_4_5",
    0x06: "CR_LI_4_6",
    0x07: "CR_LI_4_7",
}

SX128x_OPCODE_CONTENT = {
    SX1280_RADIO_GET_STATUS: [
        STATUS_CONFIG
    ],
    SX1280_RADIO_SET_SLEEP: [
        [
            (2, 2, ["IRAM Flush", "IRAM Retention"]),
            (1, 1, ["BUFF Flush", "BUFF Retention"]),
            (0, 0, ["DRAM Flush", "DRAM Retention"]),
        ]
    ],
    SX1280_RADIO_SET_STANDBY: [
        [(7, 0, {"values": {0:"STDBY_RC@13MHz RC", 1:"STDBY_XOSC@52MHz XTAL"}})]
    ],
    SX1280_RADIO_SET_TX: [
        [( 7, 0, {"name": "Base", "values": {0: "15.625 μs", 1:"62.5 μs", 2:"1ms", 3:"4ms"}})],
        [(15, 0, {"name": "BaseCount"})]
    ],
    SX1280_RADIO_SET_RX: [
        [( 7, 0, {"name": "Base", "values": {0: "15.625 μs", 1:"62.5 μs", 2:"1ms", 3:"4ms"}})],
        [(15, 0, {"name": "BaseCount"})],
    ],
    SX1280_RADIO_SET_RXDUTYCYCLE: [
        [( 7, 0, {"name": "Base", "values": {0: "15.625 μs", 1:"62.5 μs", 2:"1ms", 3:"4ms"}})],
        [(15, 0, {"name": "BaseCount"})],
        [(15, 0, {"name": "SleepCount"})],
    ],
    SX1280_RADIO_SET_LONGPREAMBLE: [
        [( 7, 0, {"name": "Long Preamble", "values": {0: "DISABLED", 1:"ENABLED"}})],
    ],
    SX1280_RADIO_SET_AUTOTX: [
        [(15, 0, {"name": "Time"})],
    ],
    SX1280_RADIO_SET_AUTOFS: [
        [(7, 0, {"name": "AutoFS", "values": {0: "False", 1:"True"}})],
    ],
    SX1280_RADIO_SET_PACKETTYPE: [
        PACKET_TYPE_CONFIG,
    ],
    SX1280_RADIO_GET_PACKETTYPE: [
        STATUS_CONFIG,
        PACKET_TYPE_CONFIG,
    ],
    SX1280_RADIO_SET_RFFREQUENCY: [
        [(23, 0, {"name": "Freq", "fmt":"{:.0f}", "eval":f"{{}}*{SX128X_FREQ_STEP}"})]
    ],
    SX1280_RADIO_SET_TXPARAMS: [
        [(7, 0, {"name": "Power", "eval":"-18 + {}"})],
        [(7, 0, {"name": "RampTime", "values": {0x00:"2us", 0x20:"4us", 0x40:"6us", 0x80:"10us",
                                                0xA0:"12us", 0xC0:"16us", 0xE0:"20us"}})],
    ],
    SX1280_RADIO_SET_CADPARAMS: [
        [(7, 0, {"name": "CAD symbols", "values": {0x00:"1", 0x20:"2", 0x40:"4", 0x60:"8", 0x80:"16"}})]
    ],
    SX1280_RADIO_SET_BUFFERBASEADDRESS: [
        [(7, 0, {"name": "TX base"})],
        [(7, 0, {"name": "RX base"})],
    ],

    SX1280_RADIO_SET_MODULATIONPARAMS: [  # Default handler
        [(7, 0, {"name": "Param0"})],
        [(7, 0, {"name": "Param1"})],
        [(7, 0, {"name": "Param2"})],
    ],
    f"{SX1280_RADIO_SET_MODULATIONPARAMS}_GFSK": [
        [(7, 0, {"name": "BitrateBandwidth", "values": GFSK_BLE_BR_CONFIG})],
        [(7, 0, {"name": "ModulationIndex", "values": GFSK_BLE_MOD_CONFIG})],
        [(7, 0, {"name": "ModulationShaping", "values": GFSK_BLE_FLRC_BT_CONFIG})],
    ],
    f"{SX1280_RADIO_SET_MODULATIONPARAMS}_BLE": [
        [(7, 0, {"name": "BitrateBandwidth", "values": GFSK_BLE_BR_CONFIG})],
        [(7, 0, {"name": "ModulationIndex", "values": GFSK_BLE_MOD_CONFIG})],
        [(7, 0, {"name": "ModulationShaping", "values": GFSK_BLE_FLRC_BT_CONFIG})],
    ],
    f"{SX1280_RADIO_SET_MODULATIONPARAMS}_FLRC": [
        [(7, 0, {"name": "BitrateBandwidth", "values": FLRC_BR_CONFIG})],
        [(7, 0, {"name": "CodingRate", "values": FLRC_CR_CONFIG})],
        [(7, 0, {"name": "ModulationShaping", "values": GFSK_BLE_FLRC_BT_CONFIG})],
    ],
    f"{SX1280_RADIO_SET_MODULATIONPARAMS}_LORA": [
        [(7, 0, {"name": "SpreadingFactor", "values": LORA_SF_CONFIG})],
        [(7, 0, {"name": "Bandwidth", "values": LORA_BW_CONFIG})],
        [(7, 0, {"name": "CodingRate", "values": LORA_CR_CONFIG})],
    ],
    f"{SX1280_RADIO_SET_MODULATIONPARAMS}_RANGING": [
        [(7, 0, {"name": "SpreadingFactor", "values": LORA_SF_CONFIG})],
        [(7, 0, {"name": "Bandwidth", "values": LORA_BW_CONFIG})],
        [(7, 0, {"name": "CodingRate", "values": LORA_CR_CONFIG})],
    ],

    SX1280_RADIO_SET_PACKETPARAMS: [  # Default handler
        [(7, 0, {"name": "Param1"})],
        [(7, 0, {"name": "Param2"})],
        [(7, 0, {"name": "Param3"})],
        [(7, 0, {"name": "Param4"})],
        [(7, 0, {"name": "Param5"})],
        [(7, 0, {"name": "Param6"})],
        [(7, 0, {"name": "Param7"})],
    ],
    f"{SX1280_RADIO_SET_PACKETPARAMS}_GFSK": [
        [(7, 0, {"name": "PreambleLength"})],
        [(7, 0, {"name": "SyncWordLength"})],
        [(7, 0, {"name": "SyncWordMatch"})],
        [(7, 0, {"name": "HeaderType"})],
        [(7, 0, {"name": "PayloadLength"})],
        [(7, 0, {"name": "CrcLength"})],
        [(7, 0, {"name": "Whitening"})],
    ],
    f"{SX1280_RADIO_SET_PACKETPARAMS}_FLRC": [
        [(7, 0, {"name": "PreambleLength"})],
        [(7, 0, {"name": "SyncWordLength"})],
        [(7, 0, {"name": "SyncWordMatch"})],
        [(7, 0, {"name": "HeaderType", "values": {0:"VARIABLE", 1:"FIXED"}})],
        [(7, 0, {"name": "PayloadLength"})],
        [(7, 0, {"name": "CrcLength"})],
        [(7, 0, {"name": "Whitening"})],
    ],
    f"{SX1280_RADIO_SET_PACKETPARAMS}_BLE": [
        [(7, 0, {"name": "ConnectionState"})],
        [(7, 0, {"name": "CrcLength"})],
        [(7, 0, {"name": "BleTestPayload"})],
        [(7, 0, {"name": "Whitening"})],
    ],
    f"{SX1280_RADIO_SET_PACKETPARAMS}_LORA": [
        [(7, 0, {"name": "PreambleLength"})],
        [(7, 0, {"name": "HeaderType"})],
        [(7, 0, {"name": "PayloadLength"})],
        [(7, 0, {"name": "CRC"})],
        [(7, 0, {"name": "InvertIQ/chirp invert"})],
    ],
    f"{SX1280_RADIO_SET_PACKETPARAMS}_RANGING": [
        [(7, 0, {"name": "PreambleLength"})],
        [(7, 0, {"name": "HeaderType"})],
        [(7, 0, {"name": "PayloadLength"})],
        [(7, 0, {"name": "CRC"})],
        [(7, 0, {"name": "InvertIQ/chirp invert"})],
    ],

    SX1280_RADIO_GET_RXBUFFERSTATUS: [
        STATUS_CONFIG,
        [(7, 0, {"name": "RX payload len"})],
        [(7, 0, {"name": "RX start ptr"})],
    ],
    SX1280_RADIO_GET_PACKETSTATUS: [
        STATUS_CONFIG,
        [(7, 0, {"name": "RFU"})],
        [(7, 0, {"name": "rssiSync, dBm", "eval":"-{}/2"})],
        [(7, 0, {"name": "errors"})],
        [(7, 0, {"name": "status"})],
        [(7, 0, {"name": "sync"})],
    ],
    f"{SX1280_RADIO_GET_PACKETSTATUS}_LORA": [
        [(7, 0, {"name": "rssiSync, dBm", "eval":"-{}/2"})],
        [(7, 0, {"name": "snr, dB", "eval":"{}/4"})],
    ],
    f"{SX1280_RADIO_GET_PACKETSTATUS}_RANGING": [
        [(7, 0, {"name": "rssiSync, dBm", "eval":"-{}/2"})],
        [(7, 0, {"name": "snr, dB", "eval":"{}/4"})],
    ],
    SX1280_RADIO_GET_RSSIINST: [
        STATUS_CONFIG,
        [(7, 0, {"name": "RSSI, dBm", "eval":"-{}/2"})],
    ],

    SX1280_RADIO_SET_DIOIRQPARAMS: [
        DIOIRQ_CONFIG,  # IRQ MASK
        DIOIRQ_CONFIG,  # DIO1
        DIOIRQ_CONFIG,  # DIO2
        DIOIRQ_CONFIG,  # DIO3
    ],
    SX1280_RADIO_GET_IRQSTATUS: [
        STATUS_CONFIG,
        DIOIRQ_CONFIG,
    ],
    SX1280_RADIO_CLR_IRQSTATUS: [
        DIOIRQ_CONFIG,
    ],

    SX1280_RADIO_SET_REGULATORMODE: [
        [(7, 0, {"name": "REG mode", "values": {0:"LDO", 1:"DCDC"}})],
    ],

    SX1280_RADIO_SET_SAVECONTEXT: [],

    SX1280_RADIO_SET_LONGPREAMBLE: [
        [(7, 0, {"name": "Long Preamble", "values": {0:"Disabled", 1:"Enabled"}})],
    ],

    SX1280_RADIO_SET_PERF_COUNTER_MODE: [
        [(7, 0, {"name": "Perf Counter Mode"})],
    ],

    SX1280_RADIO_SET_RANGING_ROLE: [
        [(7, 0, {"name": "Ranging Role", "values": {0:"Slave", 1:"Master"}})],
    ],
}

def SX128x_Opcode_Content_get(id, type=""):
    temp = f"{id}_{type}"
    if temp in SX128x_OPCODE_CONTENT:
        id = temp
    return SX128x_OPCODE_CONTENT.get(id, [])
