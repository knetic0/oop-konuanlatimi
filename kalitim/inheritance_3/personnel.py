from abc import ABC, abstractmethod
import datetime

class Personnel(ABC):
    def __init__(self, personnel_id, personnel_first_name, personnel_last_name, personnel_age, personnel_position, personnel_experience):
        self.__personnel_id = personnel_id
        self._personnel_first_name = personnel_first_name
        self._personnel_last_name = personnel_last_name
        self._personnel_age = personnel_age
        self._personnel_position = personnel_position
        self._personnel_experience = personnel_experience
    
    @property
    def personnel_id(self):
        return f"{self.__personnel_id}"

    @personnel_id.setter
    def personnel_id(self, new_value):
        raise AttributeError("You can't Change ID. Read-only!")
    
    @property
    def personnel_first_name(self):
        return f"{self._personnel_first_name}"
    
    @personnel_first_name.setter
    def personnel_first_name(self, new_value):
        self._personnel_first_name = new_value
        return f"{self._personnel_first_name}"
    
    @property
    def personnel_last_name(self):
        return f"{self._personnel_last_name}"
    
    @personnel_last_name.setter
    def personnel_last_name(self, new_value):
        self._personnel_last_name = new_value
        return f"{self._personnel_last_name}"
    
    @property
    def personnel_age(self):
        return f"{self._personnel_age}"
    
    @personnel_age.setter
    def personnel_age(self, new_value):
        self._personnel_age = new_value
        
    @property
    def personnel_position(self):
        return f"{self._personnel_position}"
    
    @personnel_position.setter
    def personnel_position(self, new_value):
        self._personnel_position = new_value
        return f"{self._personnel_position}"
    
    @property
    def personnel_experience(self):
        return self.calc_experience(self._personnel_experience)
    
    @personnel_experience.setter
    def personnel_experience(self, new_value):
        self._personnel_experience = new_value
        return self.calc_experience(self._personnel_experience)
    
    @property
    def print_all(self):
        return f"ID : {self.personnel_id} \t Name : {self.personnel_first_name} \t Surname : {self.personnel_last_name} \t Age : {self.personnel_age} \t Position : {self.personnel_position} \t Experience : {self.personnel_experience} \n"
    
    @abstractmethod
    def get_salary(self):
        pass 
    
    @staticmethod
    def calc_experience(experience):
        return datetime.date.today().year - experience