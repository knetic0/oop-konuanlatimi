from kisi import Kisi 

class Ogretmen:
    def __init__(self, info:Kisi, salary, branch):
        self._info = info 
        self._salary = salary
        self._branch = branch 
        
    @property
    def yazdir(self):
        return f"{self._info.isim} {self._info.soyisim} {self._info.yas} {self._salary} {self._branch}"