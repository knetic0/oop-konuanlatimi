from worker import Worker 

class Janitor(Worker):
    def __init__(self, janitor_id, janitor_first_name, janitor_last_name, janitor_age, janitor_position, janitor_experience, salary, salary_ratio):
        super().__init__(janitor_id, janitor_first_name, janitor_last_name, janitor_age, janitor_position, janitor_experience, salary, salary_ratio)