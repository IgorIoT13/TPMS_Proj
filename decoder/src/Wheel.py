from .reader import get_pressure_from_byte, reader, filter_empty

class Wheel:
    def __init__(self, sensor_id, bytes_list):
        self.bytes_list = bytes_list
        self.sensor_id = sensor_id
        self.__pressure = 0

        self.k = 0.05
        self.c = - 8.35

    def check_by_id(self, bytes_input):
        storage_bytes = filter_empty(bytes_input)
        if storage_bytes and bytes_input[2] == self.bytes_list[0] and bytes_input[3] == self.bytes_list[1]:
            ready_value = get_pressure_from_byte(storage_bytes)
            self.update_pressure(ready_value)


    def update_pressure(self, byte_val):
        self.__pressure = self.__calculate_pressure(byte_val)

    def get_pressure(self):
        return self.__pressure

    def __calculate_pressure(self, byte_val):
        return self.k * byte_val + self.c

    


