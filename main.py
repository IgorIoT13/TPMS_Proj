import serial

from datetime import datetime


ser = serial.Serial(
    port='/dev/ttyUSB0', 
    baudrate=9600, 
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

iter = 0

storage_list = list()
Buffer_byte = None
Enabled = False

Enabled_list = list()

def reader():
    global Buffer_byte, Enabled, iter
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
                iter += 1
                if len(storage_list) > 4:
                    checker()
                else:
                    storage_list.clear()
                Enabled = False
            else:
                Enabled = False
            # print(data.hex())

def save_list_to_file(lst, filename="output.txt"):
    with open(filename, "a") as f:
        f.write(" ".join([x for x in lst]) + "\n")

def save_pathern(target, lst, filename="custom_data.txt", time_data=False):
    string = " ".join([x for x in lst])
    if time_data:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        string += f"| {current_time}"
    
    string += "\n"
    if target in string:
        with open(filename, "a") as f:
            f.write(string)
        
    

def checker():
    if storage_list[-1] == '79':  
        print("\n-----------------------------------------------------------")
        str_res = f"{iter}. "
        for i in storage_list:
            str_res += i + " "
        print(str_res)
                
        if len(storage_list) == 11 or len(storage_list) == 12:
            save_pathern("55 95 f6 2a", storage_list, "data_1.txt", time_data=True)
            save_pathern("55 95 e0 a9", storage_list, "data_2.txt", time_data=True)
            # save_pathern("55 95 f6 2a", storage_list, "data_3.txt", time_data=True)
            save_list_to_file(storage_list, "all_data.txt")
        storage_list.clear()
        

reader()

