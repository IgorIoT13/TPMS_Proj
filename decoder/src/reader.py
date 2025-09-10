import serial

ser = serial.Serial(
    port='/dev/ttyUSB0', 
    baudrate=9600, 
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

def reader():
    storage_list = list()
    Buffer_byte = None
    Enabled = False

    Enabled_list = list()
    while True:
        data = ser.read(1)
        if data:
            if data.hex() == '55':
                Buffer_byte = data
            elif Buffer_byte and data.hex() == '95':
                storage_list.clear()
                storage_list.append(Buffer_byte.hex())
                storage_list.append(data.hex())
                Buffer_byte = None
                Enabled = True
            elif data.hex() != '79' and Enabled:
                storage_list.append(data.hex())
            elif data.hex() == '79' and Enabled:
                storage_list.append(data.hex())
                if len(storage_list) == 11 or len(storage_list) == 12:
                    return storage_list
                else:
                    storage_list.clear()
                Enabled = False
            else:
                Enabled = False


def filter_empty(storage_list):
    if storage_list != ['55', '95', '00', '00', '00', '00', '00', '00', '01', '00', '79'] and storage_list[-1] == '79':
        return storage_list
    return None


def get_pressure_from_byte(storage_list):
    if storage_list and len(storage_list) > 4 and storage_list[-1] == '79':
        pressure_byte = storage_list[-2]
        byte_val = int(pressure_byte, 16)
        # Формула з Wheel: pressure = 0.04 * byte_val - 7.62
        return byte_val
    return 0