class Address:
    def __init__(self, city, town):
        self.city = city
        self.town = town 
    
    @property
    def print_address(self):
        return f"City : {self.city} \t Town : {self.town}"