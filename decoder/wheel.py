class Wheel:
    def __init__(self, id, file_name, start_value=0):
        self.id = id
        self.file_name = file_name
        self.value = start_value

    def read(self):
        with open(self.file_name, 'r') as file:
            return file.read()
        
    def get_value(self):
        return float(self.value)
    
    def set_pressure(self, pressure):
        # with open(self.file_name, 'w') as file:
        #     file.write(f"{pressure:.2f}")
        # self.value = pressure
        self.value = pressure
    
    def json(self):
        return {
            'id': self.id,
            'value': self.get_value()
        }
    
    
