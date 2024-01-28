import struct

from pymodbus.client import ModbusTcpClient

from .consts import *


class ShellyProModbusClient:

    @staticmethod
    def __group_registers(r):
        return b''.join(struct.pack('<H', val) for val in r)

    @classmethod
    def _decode_string(cls, v):
        """ Decode string data from registers list"""
        return cls.__group_registers(v).replace(b"\x00", b"").decode("ascii")

    @classmethod
    def _decode_int32(cls, v):
        decoded = struct.unpack('<I', cls.__group_registers(v))
        return decoded[0]

    @classmethod
    def _decode_boolean(cls, v):
        if v == 1:
            return True
        else:
            return False

    def __init__(self, ip, rounding=2, set_property=True):
        self.ip_address = ip
        self._client = ModbusTcpClient(self.ip_address)
        self._rounding = rounding # nb decimals for float number
        self.__mac = None
        self.__name = None
        self.__model = None
        self.__version = 0
        self.connect(set_property=set_property)

    def __del__(self):
        try:
            self._client.close()
        except Exception as e:
            print(e)

    def connect(self, set_property=True):
        self._client.connect()
        if set_property:
            try:
                registers = self._query_register(0, count=16)  # Get all symbols in one call
                self.__mac = self._decode_string(registers[:6])
                self.__model = self._decode_string(registers[6:])
            except ValueError:
                raise ValueError("Unable to init device values")

    @property
    def mac(self):
        if self.__mac:
            return self.__mac
        else:
            self.__mac = self.read_string_value(DEVICE_MAC_REGISTER[0], DEVICE_MAC_REGISTER[1])
            return self.__mac

    @property
    def model(self):
        if self.__model:
            return self.__model
        else:
            self.__model = self.read_string_value(DEVICE_MODEL_REGISTER[0], DEVICE_MODEL_REGISTER[1])
            return self.__model

    @property
    def name(self):
        if self.__name:
            return self.__name
        else:
            self.__name = self.read_string_value(DEVICE_NAME_REGISTER[0], DEVICE_NAME_REGISTER[1])
            return self.__name

    @property
    def data_version(self):
        """ EM or EM1 data format
            EM = 0
            EM1 = 1
        """
        return MODEL_VERSION_MAPPING.get(self.model, 0)

    def _decode_float(self, v, rounding=2):
        decoded_float = struct.unpack('<f', self.__group_registers(v))
        r = rounding or self._rounding
        return round(decoded_float[0], r)

    def _query_register(self, address, count=1):
        response = self._client.read_input_registers(address, count=count)
        if not response.isError():
            return response.registers
        else:
            raise ValueError(f"Unable to query register {address}")

    def _query_coil(self, address, count=1):
        response = self._client.read_coils(address, count=count)
        # print(response)
        if not response.isError():
            return response.registers
        else:
            raise ValueError(f"Unable to query coil {address}")

    def _write_coil(self, address, v=True):
        response = self._client.write_coil(address, v)
        print(response)
        if not response.isError():
            return response
        else:
            raise ValueError(f"Unable to write coil {address}")

    def read_boolean_value(self, address):
        response = self._query_register(address)
        return self._decode_boolean(response[0])

    def read_uint32_value(self, address):
        response = self._query_register(address, count=2)
        return self._decode_int32(response)

    def read_float_value(self, address, rounding=2):
        response = self._query_register(address, count=2)
        return self._decode_float(response, rounding=rounding)

    def read_string_value(self, address, length):
        response = self._query_register(address, count=length)
        return self._decode_string(response)

    def read_metrics(self, list_metrics, offset=0):
        """
        Read multiples metrics in only one register holding call
        :param list_metrics: list of tuples in format [(<modbustcp_address>, <count>, <metric_type>, <metric_name>)]
        :param offset: offset to add to address register when multiple component of same type exists
        :return: generator of tuple of metric formated as (<metric_name>, <metric_value>)
        """
        start_reg = list_metrics[0][0] + offset # First address of metric list
        end_reg = list_metrics[-1][0] + list_metrics[-1][1] + offset # Address of last metric plus the length of the last metric
        register_count = end_reg - start_reg
        # if register_count < 16: # Case that the metric list is too big
        reg = self._query_register(start_reg, count=register_count)
        for i, metric in enumerate(list_metrics):
            metric_address = metric[0] + offset
            metric_type = metric[2]
            metric_unit = metric[3]
            metric_name = metric[4]
            if metric_type == "boolean":
                value = self._decode_boolean(reg[metric_address - start_reg])
            else:
                start = metric_address - start_reg
                end = metric_address - start_reg + metric[1]
                if metric_type == "uint32":
                    value = self._decode_int32(reg[start:end])
                elif metric_type == "float":
                    value = self._decode_float(reg[start:end])
                elif metric_type == "string":
                    value = self._decode_string(reg[start:end])
                else: # Omit the metric if the type is unknown (might raise a warning but not efficient on for)
                    continue
            yield metric_address, value, metric_unit, metric_name

    def _get_device_registers(self):
        try:
            device_registers = MODEL_DATA_REGISTERS[self.data_version]
            return device_registers
        except KeyError:
            raise NotImplementedError(f"Data model is not supported for device data version {self.data_version}")

    def get_energy_meter(self, index=0):
        r = self._get_device_registers()
        offset = r["em"][1] * index
        registers = r["em"][0]
        return self.read_metrics(registers, offset=offset)
        # return {m[3]: {"value": m[1], "unit": m[2]} for m in metrics}

    def get_em(self, **kwargs):
        """ Alias """
        return self.get_energy_meter(**kwargs)

    def get_energy_data(self, index=0):
        r = self._get_device_registers()
        offset = r["emdata"][1] * index
        registers = r["emdata"][0]
        return self.read_metrics(registers, offset=offset)

    def get_emdata(self, **kwargs):
        """ Alias """
        return self.get_energy_data(**kwargs)