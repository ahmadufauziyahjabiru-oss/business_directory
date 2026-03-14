from datetime import datetime

class Business:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.time_added = datetime.now()

    def display(self):
        return f"{self.name} - {self.location}"