from src import Wheel, reader, filter_empty, sent_data, write_wheel_data
from display_sent import get_ready_message

import time


def main_thread():
    print(get_ready_message("1", "2,2 atm"))

    sent_data(get_ready_message("2", "2,2 atm"))


    wheel1 = Wheel(sensor_id=1, bytes_list=['f6', '2a'])
    wheel2 = Wheel(sensor_id=2, bytes_list=['e0', 'a9'])
    # wheel3 = Wheel(sensor_id=1, bytes_list=['f7', '23'])
    # wheel4 = Wheel(sensor_id=2, bytes_list=['83', 'a1'])
    wheel2.c -= 1.6

    data = wheel1.get_pressure()
    data2 = wheel2.get_pressure()

    write_wheel_data('../gen_data/wheel_1.txt', data)
    write_wheel_data('../gen_data/wheel_2.txt', data2)
    write_wheel_data('../gen_data/wheel_3.txt', 2.5)
    write_wheel_data('../gen_data/wheel_4.txt', 2.3)

    while True:
        bytes_data = reader()
        if bytes_data:
            wheel1.check_by_id(bytes_data)
            wheel2.check_by_id(bytes_data)

            print(f"Wheel 1 Pressure: {wheel1.get_pressure():.2f} atm")
            print(f"Wheel 2 Pressure: {wheel2.get_pressure():.2f} atm")
            print("-----")

            if data != wheel1.get_pressure():
                print(f"Wheel 1 update {data:.2f} atm")
                data = wheel1.get_pressure()
                print(f"Wheel 1 Pressure: {data:.2f} atm")
                write_wheel_data('../gen_data/wheel_1.txt', data)
                sent_data(get_ready_message("1", f"{data:.2f} atm"))

            if data2 != wheel2.get_pressure():
                print(f"Wheel 2 update {data2:.2f} atm")
                data2 = wheel2.get_pressure()
                print(f"Wheel 2 Pressure: {data2:.2f} atm")
                write_wheel_data('../gen_data/wheel_2.txt', data2)
                sent_data(get_ready_message("2", f"{data2:.2f} atm")) 
        time.sleep(1)


if __name__ == "__main__":
    main_thread()