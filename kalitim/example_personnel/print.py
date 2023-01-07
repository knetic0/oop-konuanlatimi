class Print:
    def __init__(self):
        self.personnel_list = []
    
    def add(self, personnel):
        self.personnel_list.append(personnel)
        
    def print(self):
        for person in self.personnel_list:
            print(f"{person.print_information} \n {person.get_salary()} \n {person.print_address} \n")