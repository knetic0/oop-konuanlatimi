class Payroll:
    def __init__(self):
        self.employee_list = []
    
    def add(self, employee):
        self.employee_list.append(employee) # employee_list'e siniflar eklenir.
        
    def print(self):
        print(self.employee_list) # [<emp.FullTimeEmployee object at 0x10ef7f6d0>, <emp2.HourlyEmployee object at 0x10efc78e0>]
        for emp in self.employee_list: # emp = FullTimeEmployee
            print(f"{emp.full_name} \t ${emp.get_salary()}")