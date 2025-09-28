class Wheel:
    def __init__(self, id, file_name):
        self.id = id
        self.file_name = file_name
        self.value = 0

    def read(self):
        with open(self.file_name, 'r') as file:
            return file.read()
        
    def get_value(self):
        return float(self.read())
    
    def set_pressure(self, pressure):
        with open(self.file_name, 'w') as file:
            file.write(f"{pressure:.2f}")
        self.value = pressure
    
    def json(self):
        return {
            'id': self.id,
            'value': self.get_value()
        }
    
    
