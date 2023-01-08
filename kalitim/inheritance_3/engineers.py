from worker import Worker

class Engineer(Worker):
    def __init__(self, eng_id, eng_first_name, eng_last_name, eng_age, eng_position, eng_experience, salary, salary_ratio):
        super().__init__(eng_id, eng_first_name, eng_last_name, eng_age, eng_position, eng_experience, salary, salary_ratio)

    