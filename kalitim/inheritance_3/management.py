from personnel import Personnel

class Management(Personnel):
    def __init__(self, management_id, management_first_name, management_last_name, management_age, management_position, management_experience, management_salary, management_salary_ratio):
        super().__init__(management_id, management_first_name, management_last_name, management_age, management_position, management_experience)
        self._management_salary = management_salary
        self._management_salary_ratio = management_salary_ratio
        
    def get_salary(self):
        return f"Your (Mr / Mr's {self.personnel_first_name + self.personnel_last_name}) Salary is : {self._management_salary * self._management_salary_ratio}"