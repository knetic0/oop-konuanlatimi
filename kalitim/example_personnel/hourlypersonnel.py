from inheritance import Personnel
from address import Address

class HourlyPersonnel(Personnel, Address):
    def __init__(self, first_name, last_name, id_number, h_salary, hours, city, town):
        Address.__init__(self, city, town)
        Personnel.__init__(self, first_name, last_name, id_number)
        self.h_salary = h_salary
        self.hours = hours
        
    def get_salary(self):
        calc = self.h_salary * self.hours
        return f"{self.first_name}'s Salary is : {calc}"
