class Personnel:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name 
        self.id_number = id_number
        
    @property
    def print_information(self):
        return f"Name : {self.first_name} \t Surname : {self.last_name} \t ID : {self.id_number}"
            