from personnel import Personnel

class Worker(Personnel):
    def __init__(self, worker_id, worker_first_name, worker_last_name, worker_age, worker_position, worker_experience, salary, salary_ratio):
        super().__init__(worker_id, worker_first_name, worker_last_name, worker_age, worker_position, worker_experience)
        self._salary = salary 
        self._salary_ratio = salary_ratio
        
    def get_salary(self):
        return f"Your (Mr / Mr's {self.personnel_first_name + self.personnel_last_name}) Salary is : {self._salary * self._salary_ratio}"