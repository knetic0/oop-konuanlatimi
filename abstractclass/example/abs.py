from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name 
        
    @property
    def full_name(self): # property full_name / isim ve soyisimi dondurur.
        return f"{self.first_name} {self.last_name}"
    
    @abstractmethod # abstractmethod 
    def get_salary(self):
        pass