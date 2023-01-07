from inheritance import Personnel
from address import Address

class Manager(Personnel, Address):
    def __init__(self, first_name, last_name, id_number, salary, city, town):
        Personnel.__init__(self, first_name, last_name, id_number)
        Address.__init__(self, city, town)
        self.salary = salary 
    
    def get_salary(self):
        return f"{self.first_name}'s Salary is : {self.salary}"


