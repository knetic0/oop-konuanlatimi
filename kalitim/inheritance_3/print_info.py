import os 
import json

class Print:
    def __init__(self):
        self._list_worker = []
        
    def add(self, worker):
        self._list_worker.append(worker)
        
    def print(self):
        for work in self._list_worker:
            print(work.print_all, work.get_salary())
            print("*"*30)
    
    def file_handling(self):
        os.chdir(f"{os.getcwd()}" + "/final/inheritance_3")
        if "result.json" not in os.listdir():
            with open("result.json", 'a') as f:
                for work in self._list_worker:
                    temp = {
                        "id": work.personnel_id,
                        "name": work.personnel_first_name,
                        "surname": work.personnel_last_name,
                        "age": work.personnel_age,
                        "position": work.personnel_position,
                        "experience": work.personnel_experience,
                        "salary": work.get_salary(),
                    }
                    temp_json = json.dumps(temp, indent=2)
                    f.write(temp_json)
                f.close()