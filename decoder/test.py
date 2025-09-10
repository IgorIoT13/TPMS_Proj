from src import Wheel, reader, filter_empty

def main():
    wheel1 = Wheel(sensor_id=1, bytes_list=['f6', '2a'])
    wheel2 = Wheel(sensor_id=2, bytes_list=['e0', 'a9'])
    wheel2.c -= 1.6


    while True:
        bytes_data = reader()
        if bytes_data:
            wheel1.check_by_id(bytes_data)
            wheel2.check_by_id(bytes_data)
            # wheel3.check_by_id(bytes_data)
            # wheel4.check_by_id(bytes_data)

            print(f"Wheel 1 Pressure: {wheel1.get_pressure()} psi")
            print(f"Wheel 2 Pressure: {wheel2.get_pressure()} psi")
            # print(f"Wheel 3 Pressure: {wheel3.get_pressure()} psi")
            # print(f"Wheel 4 Pressure: {wheel4.get_pressure()} psi")
            print("-----")    


if __name__ == "__main__":
    main()