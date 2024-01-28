
DEVICE_MAC_REGISTER = (0, 6)
DEVICE_MODEL_REGISTER = (6, 10)
DEVICE_NAME_REGISTER = (16, 32)

EM_COMPONENT_OFFSET = 80
EM1_COMPONENT_OFFSET = 20
EMDATA_COMPONENT_OFFSET = 70
EM1DATA_COMPONENT_OFFSET = 20

EM_REGISTERS = [
    (1000, 2, "uint32", None, "Timestamp of the last update"),
    (1002, 1, "boolean", None, "Phase A meter error"),
    (1003, 1, "boolean", None, "Phase B meter error"),
    (1004, 1, "boolean", None, "Phase C meter error"),
    (1005, 1, "boolean", None, "Neutral meter error"),
    (1006, 1, "boolean", None, "Phase sequence error"),
    (1007, 2, "float", None, "Neutral current, A"),
    (1009, 1, "boolean", None, "Neutral current mismatch"),
    (1010, 1, "boolean", None, "Neutral overcurrent error"),
    (1011, 2, "float", "A", "Total current"),
    (1013, 2, "float", "W", "Total active power"),
    (1015, 2, "float", "VA", "Total apparent power"),
    (1020, 2, "float", "V", "Phase A voltage"),
    (1022, 2, "float", "A", "Phase A current"),
    (1024, 2, "float", "W", "Phase A active power"),
    (1026, 2, "float", "VA", "Phase A apparent power"),
    (1028, 2, "float", None, "Phase A power factor"),
    (1030, 1, "boolean", None, "Phase A overpower error"),
    (1031, 1, "boolean", None, "Phase A overvoltage error"),
    (1032, 1, "boolean", None, "Phase A overcurrent error"),
    (1040, 2, "float", "V", "Phase B voltage"),
    (1042, 2, "float", "A", "Phase B current"),
    (1044, 2, "float", "W", "Phase B active power"),
    (1046, 2, "float", "VA", "Phase B apparent power"),
    (1048, 2, "float", None, "Phase B power factor"),
    (1050, 1, "boolean", None, "Phase B overpower error"),
    (1051, 1, "boolean", None, "Phase B overvoltage error"),
    (1052, 1, "boolean", None, "Phase B overcurrent error"),
    (1060, 2, "float", "V", "Phase C voltage"),
    (1062, 2, "float", "A", "Phase C current"),
    (1064, 2, "float", "W", "Phase C active power"),
    (1066, 2, "float", "VA", "Phase C apparent power"),
    (1068, 2, "float", None, "Phase C power factor"),
    (1070, 1, "boolean", None, "Phase C overpower error"),
    (1071, 1, "boolean", None, "Phase C overvoltage error"),
    (1072, 1, "boolean", None, "Phase C overcurrent error")
]
EM1_REGISTERS = [
    (2000, 2, "uint32", None, "Timestamp of the last update"),
    (2002, 1, "boolean", None, "EM1 error"),
    (2003, 2, "float", "V", "Voltage"),
    (2005, 2, "float", "A", "Current"),
    (2007, 2, "float", "W", "Active power"),
    (2009, 2, "float", "VA", "Apparent power"),
    (2011, 2, "float", None, "Power factor"),
    (2013, 1, "boolean", None, "Overpower error"),
    (2014, 1, "boolean", None, "Overvoltage error"),
    (2015, 1, "boolean", None, "Overcurrent error")
]
EMDATA_REGISTERS = [
    (1160, 2, "uint32", None, "Timestamp of the last update"),
    (1162, 2, "float", "Wh", "Total active energy accumulated for all phases - perpetual count"),
    (1164, 2, "float", "Wh", "Total active returned energy accumulated for all phases - perpetual count"),
    (1170, 2, "float", "Wh", "Phase A total active energy"),
    (1172, 2, "float", "Wh", "Phase A fundamental active energy"),
    (1174, 2, "float", "Wh", "Phase A total active returned energy"),
    (1176, 2, "float", "Wh", "Phase A fundamental active returned energy"),
    (1178, 2, "float", "VARh", "Phase A lagging reactive energy"),
    (1180, 2, "float", "VARh", "Phase A leading reactive energy"),
    (1182, 2, "float", "Wh", "Phase A total active energy - perpetual count"),
    (1184, 2, "float", "Wh", "Phase A total active returned energy - perpetual count"),
    (1190, 2, "float", "Wh", "Phase B total active energy"),
    (1192, 2, "float", "Wh", "Phase B fundamental active energy"),
    (1194, 2, "float", "Wh", "Phase B total active returned energy"),
    (1196, 2, "float", "Wh", "Phase B fundamental active returned energy"),
    (1198, 2, "float", "VARh", "Phase B lagging reactive energy"),
    (1200, 2, "float", "VARh", "Phase B leading reactive energy"),
    (1202, 2, "float", "Wh", "Phase B total active energy - perpetual count"),
    (1204, 2, "float", "Wh", "Phase B total active returned energy - perpetual count"),
    (1210, 2, "float", "Wh", "Phase C total active energy"),
    (1212, 2, "float", "Wh", "Phase C fundamental active energy"),
    (1214, 2, "float", "Wh", "Phase C total active returned energy"),
    (1216, 2, "float", "Wh", "Phase C fundamental active returned energy"),
    (1218, 2, "float", "VARh", "Phase C lagging reactive energy"),
    (1220, 2, "float", "VARh", "Phase C leading reactive energy"),
    (1222, 2, "float", "Wh", "Phase C total active energy - perpetual count"),
    (1224, 2, "float", "Wh", "Phase C total active returned energy - perpetual count")
]
EM1DATA_REGISTERS = [
    (2300, 2, "uint32", None, "Timestamp of the last update"),
    (2302, 2, "float", "Wh", "Total active energy"),
    (2304, 2, "float", "Wh", "Total active returned energy"),
    (2306, 2, "float", "VARh", "Lagging reactive energy"),
    (2308, 2, "float", "VARh", "Leading reactive energy"),
    (2310, 2, "float", "Wh", "Total active energy - perpetual count"),
    (2312, 2, "float", "Wh", "Total active returned energy - perpetual count")
]

# Mapping for managing high level devices registers mapping
MODEL_VERSION_MAPPING = {"SPEM-003CEBEU": 0,
                         "SPEM-003CEBEU400": 0,
                         "SPEM-002CEBEU50": 1}

MODEL_DATA_REGISTERS = {
    0: {
        "em": (EM_REGISTERS, EM_COMPONENT_OFFSET),
        "emdata": (EMDATA_REGISTERS, EMDATA_COMPONENT_OFFSET)
    },
    1: {
        "em": (EM1_REGISTERS, EM1_COMPONENT_OFFSET),
        "emdata": (EM1DATA_REGISTERS, EM1DATA_COMPONENT_OFFSET)
    }
}