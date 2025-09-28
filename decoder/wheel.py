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
    
    def json(self):
        return {
            'id': self.id,
            'value': self.get_value()
        }
    
    
