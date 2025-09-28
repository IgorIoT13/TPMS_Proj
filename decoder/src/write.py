def write_wheel_data(file_name, value):
    with open(file_name, 'w') as file:
        file.write(str(value))