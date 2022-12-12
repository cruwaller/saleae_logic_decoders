
#*****************************************************************
#  SX127x GENERIC
#*****************************************************************
SX127X_FREQ_STEP                   = 61.03515625
SX127X_SPI_REG_READ                = 0x00
SX127X_SPI_REG_WRITE               = 0x80
SX127X_SPI_REG_MASK                = ~SX127X_SPI_REG_WRITE


#*****************************************************************
#  SX127x REGISTERS
#*****************************************************************
SX127X_REG_FIFO                    = 0x00
SX127X_REG_OP_MODE                 = 0x01
SX127X_REG_FRF_MSB                 = 0x06
SX127X_REG_FRF_MID                 = 0x07
SX127X_REG_FRF_LSB                 = 0x08
SX127X_REG_PA_CONFIG               = 0x09
SX127X_REG_PA_RAMP                 = 0x0A
SX127X_REG_OCP                     = 0x0B
SX127X_REG_LNA                     = 0x0C
SX127X_REG_FIFO_ADDR_PTR           = 0x0D
SX127X_REG_FIFO_TX_BASE_ADDR       = 0x0E
SX127X_REG_FIFO_RX_BASE_ADDR       = 0x0F
SX127X_REG_FIFO_RX_CURRENT_ADDR    = 0x10
SX127X_REG_IRQ_FLAGS_MASK          = 0x11
SX127X_REG_IRQ_FLAGS               = 0x12
SX127X_REG_RX_NB_BYTES             = 0x13
SX127X_REG_RX_HEADER_CNT_VALUE_MSB = 0x14
SX127X_REG_RX_HEADER_CNT_VALUE_LSB = 0x15
SX127X_REG_RX_PACKET_CNT_VALUE_MSB = 0x16
SX127X_REG_RX_PACKET_CNT_VALUE_LSB = 0x17
SX127X_REG_MODEM_STAT              = 0x18
SX127X_REG_PKT_SNR_VALUE           = 0x19
SX127X_REG_PKT_RSSI_VALUE          = 0x1A
SX127X_REG_RSSI_VALUE              = 0x1B
SX127X_REG_HOP_CHANNEL             = 0x1C
SX127X_REG_MODEM_CONFIG_1          = 0x1D
SX127X_REG_MODEM_CONFIG_2          = 0x1E
SX127X_REG_SYMB_TIMEOUT_LSB        = 0x1F
SX127X_REG_PREAMBLE_MSB            = 0x20
SX127X_REG_PREAMBLE_LSB            = 0x21
SX127X_REG_PAYLOAD_LENGTH          = 0x22
SX127X_REG_MAX_PAYLOAD_LENGTH      = 0x23
SX127X_REG_HOP_PERIOD              = 0x24
SX127X_REG_FIFO_RX_BYTE_ADDR       = 0x25
SX127X_REG_MODEM_CONFIG_3          = 0x26
SX127x_REG_PPMOFFSET               = 0x27
SX127X_REG_FEI_MSB                 = 0x28
SX127X_REG_FEI_MID                 = 0x29
SX127X_REG_FEI_LSB                 = 0x2A
SX127X_REG_RSSI_WIDEBAND           = 0x2C
SX127X_REG_DETECT_OPTIMIZE         = 0x31
SX127X_REG_INVERT_IQ               = 0x33
SX127X_REG_DETECTION_THRESHOLD     = 0x37
SX127X_REG_SYNC_WORD               = 0x39
SX127X_REG_INVERT_IQ_2             = 0x3B
SX127X_REG_DIO_MAPPING_1           = 0x40
SX127X_REG_DIO_MAPPING_2           = 0x41
SX127X_REG_VERSION                 = 0x42
SX127X_REG_TCXO                    = 0x4B
SX127X_REG_PA_DAC                  = 0x4D
SX127X_REG_AGC_REF                 = 0x61
SX127X_REG_AGC_THRESH_1            = 0x62
SX127X_REG_AGC_THRESH_2            = 0x63
SX127X_REG_AGC_THRESH_3            = 0x64
SX127X_REG_PLL                     = 0x70


#*****************************************************************
#  SX1278 SPECIFIC REGISTERS
#*****************************************************************
SX1278_REG_FORMER_TEMP             = 0x5D


SX127X_REG_NAMES = {
    SX127X_REG_FIFO: "FIFO",
    SX127X_REG_OP_MODE: "OP MODE",
    SX127X_REG_FRF_MSB: "FRF MSB",
    SX127X_REG_FRF_MID: "FRF MID",
    SX127X_REG_FRF_LSB: "FRF LSB",
    SX127X_REG_PA_CONFIG: "PA CONFIG",
    SX127X_REG_PA_RAMP: "PA RAMP",
    SX127X_REG_OCP: "OCP",
    SX127X_REG_LNA: "LNA",
    SX127X_REG_FIFO_ADDR_PTR: "FIFO ADDR PTR",
    SX127X_REG_FIFO_TX_BASE_ADDR: "FIFO TX BASE",
    SX127X_REG_FIFO_RX_BASE_ADDR: "FIFO RX BASE",
    SX127X_REG_FIFO_RX_CURRENT_ADDR: "FIFO RX CURRENT",
    SX127X_REG_IRQ_FLAGS_MASK: "IRQ FLAGS MASK",
    SX127X_REG_IRQ_FLAGS: "IRQ FLAGS",
    SX127X_REG_RX_NB_BYTES: "RX NB BYTES",
    SX127X_REG_RX_HEADER_CNT_VALUE_MSB: "RX HDR CNT MSB",
    SX127X_REG_RX_HEADER_CNT_VALUE_LSB: "RX HDR CNT LSB",
    SX127X_REG_RX_PACKET_CNT_VALUE_MSB: "RX PKT CNT MSB",
    SX127X_REG_RX_PACKET_CNT_VALUE_LSB: "RX PKT CNT LSB",
    SX127X_REG_MODEM_STAT: "MODEM STAT",
    SX127X_REG_PKT_SNR_VALUE: "PKT SNR",
    SX127X_REG_PKT_RSSI_VALUE: "PKT RSSI",
    SX127X_REG_RSSI_VALUE: "RSSI",
    SX127X_REG_HOP_CHANNEL: "HOP CHANNEL",
    SX127X_REG_MODEM_CONFIG_1: "MODEM CFG 1",
    SX127X_REG_MODEM_CONFIG_2: "MODEM CFG 2",
    SX127X_REG_SYMB_TIMEOUT_LSB: "SYMB TIMEOUT LSB",
    SX127X_REG_PREAMBLE_MSB: "PREAMBLE MSB",
    SX127X_REG_PREAMBLE_LSB: "PREAMBLE LSB",
    SX127X_REG_PAYLOAD_LENGTH: "PAYLOAD LEN",
    SX127X_REG_MAX_PAYLOAD_LENGTH: "MAX PAYLOAD LEN",
    SX127X_REG_HOP_PERIOD: "HOP PERIOD",
    SX127X_REG_FIFO_RX_BYTE_ADDR: "FIRO RX BYTE ADDR",
    SX127X_REG_MODEM_CONFIG_3: "MODEM CFG 3",
    SX127x_REG_PPMOFFSET: "PPM OFFSET",
    SX127X_REG_FEI_MSB: "FEI MSB",
    SX127X_REG_FEI_MID: "FEI MID",
    SX127X_REG_FEI_LSB: "FEI LSB",
    SX127X_REG_RSSI_WIDEBAND: "RSSI WIDEBAND",
    SX127X_REG_DETECT_OPTIMIZE: "DETECT OPTIMIZE",
    SX127X_REG_INVERT_IQ: "INVERT IQ",
    SX127X_REG_DETECTION_THRESHOLD: "DETECTION THRESHOLD",
    SX127X_REG_SYNC_WORD: "SYNC WORD",
    SX127X_REG_INVERT_IQ_2: "INVERT IQ 2",
    SX127X_REG_DIO_MAPPING_1: "DIO MAPPING 1",
    SX127X_REG_DIO_MAPPING_2: "DIO MAPPING 2",
    SX127X_REG_VERSION: "VERSION",
    SX127X_REG_TCXO: "TCXO",
    SX127X_REG_PA_DAC: "PA DAC",
    SX127X_REG_AGC_REF: "AGC REF",
    SX127X_REG_AGC_THRESH_1: "AGC THRESH 1",
    SX127X_REG_AGC_THRESH_2: "AGC THRESH 2",
    SX127X_REG_AGC_THRESH_3: "AGC THRESH 3",
    SX127X_REG_PLL: "PLL",

    #  SX1278 SPECIFIC REGISTERS
    SX1278_REG_FORMER_TEMP: "FORMER TEMP",
}

def SX127x_Reg_Name_get(val):
    # remove MSB which is register write flag
    return SX127X_REG_NAMES.get(val & SX127X_SPI_REG_MASK, "")


#*****************************************************************
#  SX127x REGISTER SETTINGS
#*****************************************************************
SX127x_REG_VALUES = {
    SX127X_REG_OP_MODE : [
        (7, 7, ["FSP_OOK", "LORA"]),
        (6, 6, ["ACCESS_SHARED_REG_OFF", "ACCESS_SHARED_REG_ON"]),
        (2, 0, ["SLEEP", "STANDBY", "FSTX", "TX", "FSRX", "RX CONTINUOUS", "RX SIGNLE", "CAD"]),
    ],
    SX127X_REG_FRF_MSB: [
        (23, 0, {"name": "Freq", "fmt":"{0:f}MHz", "eval":f"{{}}*{SX127X_FREQ_STEP}/10**6"})
    ],
    SX127X_REG_PA_CONFIG: [
        (7, 7, ["RFO", "BOOST"]),
        (6, 4, {"name": "MaxPower,dBm", "eval": "10.8+0.6*{}"}),
        (3, 0, {"name": "POWER"}),
    ],
    SX127X_REG_OCP: [
        (5, 5, ["OFF", "ON"]),
        (4, 0, {"name": "OCP I_max"})
    ],
    SX127X_REG_LNA: [
        (7, 5, ["GAIN 0", "GAIN 1", "GAIN 2", "GAIN 3", "GAIN 4", "GAIN 5", "GAIN 6", "GAIN 7"]),
        (1, 0, {0:"BOOST OFF", 0b11:"BOOST ON"}),
    ],
    SX127X_REG_MODEM_CONFIG_2: [
        (7, 4, {"fmt": "SF{}"}),
        (3, 3, ["TX SINGLE", "TX_CONT"]),
        (2, 2, ["CRC ON", "CRC OFF"]),
        (1, 0, {"name": "RX TIMEOUT MSB"}),
    ],
    SX127X_REG_SYMB_TIMEOUT_LSB: [
        (7, 0, {"name": "RX TIMEOUT LSB"}),
    ],
    SX127X_REG_MODEM_CONFIG_3: [
        (3, 3, ["RATE OPT OFF", "RATE OPT ON"]),
        (2, 2, ["AGC AUTO OFF", "AGC AUTO ON"]),
    ],
    SX127X_REG_PREAMBLE_MSB: [
        (7, 0, int)
    ],
    SX127X_REG_PREAMBLE_LSB: [
        (7, 0, int)
    ],
    SX127X_REG_DETECT_OPTIMIZE: [
        (2, 0, {"name": "DETECT_OPTIMIZE", "values": {0b101: "SF_6", 0b011: "SF_7_12"}}),
    ],
    SX127X_REG_DETECTION_THRESHOLD: [
        (7, 0, {"name": "DETECTION_THRESHOLD", "values": {0b1100: "SF_6", 0b1010: "SF_7_12"}})
    ],
    SX127X_REG_PA_DAC: [
        (2, 0, {"name": "PA_BOOST", "values": {0b100: "OFF", 0b111: "ON"}}),
    ],
    SX127X_REG_HOP_PERIOD: [
        (7, 0, int)
    ],
    SX127X_REG_DIO_MAPPING_1: [
        (7, 6, {"name": "DIO0", "values": {0: "RXDONE", 1: "TXDONE", 2: "CADDONE", 3:"-"}}),
        (5, 4, {"name": "DIO1", "values": {0: "RX TIMEOUT", 1: "FHSS CH CHANGE", 2: "CAD DETECTED", 3:"-"}}),
        (3, 2, {"name": "DIO2", "values": {0: "FHSS CH CHANGE", 1: "FHSS CH CHANGE", 2: "FHSS CH CHANGE", 3:"-"}}),
        (1, 0, {"name": "DIO3", "values": {0: "CAD DONE", 1: "VALID HDR", 2: "CRC ERROR", 3:"-"}}),
    ],
    SX127X_REG_DIO_MAPPING_2: [
        (7, 6, {"name": "DIO4", "values": {0: "CAD DETECTED", 1: "PLL LOCK", 2: "PLL LOCK", 3:"-"}}),
        (5, 4, {"name": "DIO5", "values": {0: "MODE READY", 1: "CLK OUT", 2: "CLK OUT", 3:"-"}}),
        (3, 1, {"name": "reserved"}),
        (0, 0, {"name": "MapPreambleDetect"}),
    ],
    SX127X_REG_IRQ_FLAGS: [
        (7, 7, ["", "RX TIMEOUT"]),
        (6, 6, ["", "RX DONE"]),
        (5, 5, ["", "CRC ERROR"]),
        (4, 4, ["", "VALID HDR"]),
        (3, 3, ["", "TX DONE"]),
        (2, 2, ["", "CAD DONE"]),
        (1, 1, ["", "FHSS CH CHANGE"]),
        (0, 0, ["", "CAD DETECTED"]),
    ],
    SX127X_REG_IRQ_FLAGS_MASK: [
        (7, 0, int)
    ],
    SX127X_REG_FIFO_TX_BASE_ADDR: [
        (7, 0, int)
    ],
    SX127X_REG_FIFO_RX_BASE_ADDR: [
        (7, 0, int)
    ],
    SX127X_REG_MODEM_CONFIG_1: [
        (7, 4, ["BW 7.80kHz", "BW 10.40kHz", "BW 15.60kHz", "BW 20.80kHz", "BW 31.25kHz",
                "BW 41.70kHz", "BW 62.50kHz", "BW 125kHz", "BW 250kHz", "BW 500kHz"]),
        (3, 1, ["CR?", "CR4/5", "CR4/6", "CR4/7", "CR4/8"]),
        (0, 0, ["EXPL HDR", "IMPL HDR"]),
    ],
    SX127X_REG_PKT_SNR_VALUE: [
        #(7, 0, {"name": "PKT SNR, dB", "eval":"(({0}&0x7F)-(128*({0}>>7)))/4", "store":"snr_last"})
        (7, 0, {"name": "dB", "eval":"{:d}/4"})
    ],
    SX127X_REG_PKT_RSSI_VALUE: [
        (7, 0, {"name": "dBm", "eval":"-157+{}"})
    ],

}

def SX127x_Reg_Content(id):
    return SX127x_REG_VALUES.get(id & SX127X_SPI_REG_MASK, [])
