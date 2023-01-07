'''

    Bir veya daha fazla abstractmethod tanimlamasi barindiran classlardir.
    abstractmethod ise tanimli bir method olup iceriginin olmamasi durumudur.
    Yani bir ornek vermek istersek;
        Evde mutfak olmali ama ne tarzda olacagi ya da ne kadar buyuk olacagi belirtilmez.
        Ya da okula_git() fonksiyonunu dusunelim. Okula gidilmeli ama nasil gidicelegi belirtilmez.
        
    Yani ne olursa olsun biz bu fonksiyonu kullanmaliyiz ama icerigini istedigimiz sekilde degistirebilir, yaratabiliriz.
    
    Bazi Kurallar:

        1- Abstract class'larda tanimladigimiz abstractmethod'u miras aldigimiz class'ta kullanmasak hata ile karsilasiriz. 
        Yani miras alindiginda miras aldigimiz class bu abstractmethodu kullanmali.
        
        2- Abstact Class'lar subclasslara ihtiyac duyarlar. Yani miras alinmalidirlar.
        
    Peki Neden Abstract Class ve Method kullaniyoruz ?
    
            Bir duzen oturtmus oluyoruz aslinda. Bir odeme sistemi dusunelim. Bu odeme sisteminin alt yapisi degistiginde
        Abstractclass'tan miras aldigimiz odeme_yap() abstract methodu yeni alt yapida zorunlu fonksiyon haline gelecektir.
        Hangi alt yapi kullanilirsa kullanilsin odeme_yap() fonksiyonunu bu isimde kullanmalisiniz ama icerigi degisebilir.
         

'''


from abc import ABC, abstractmethod

class Computer(ABC):
    def __init__(self, brand, cpu, ram, gpu):
        self.brand = brand 
        self.cpu = cpu 
        self.ram = ram 
        self.gpu = gpu 
    
    @property
    def print_information(self):
        return f"{self.brand} \t {self.cpu} \t {self.ram} \t {self.gpu}"
    
    @abstractmethod
    def get_price(self):
        pass     
    
class Laptop(Computer):
    def __init__(self, brand, cpu, ram, gpu, price):
        super().__init__(brand, cpu, ram, gpu)
        self.price = price 
        
    def get_price(self):
        return f"{self.brand} Laptop Price : {self.price}"
    
class Desktop(Computer):
    def __init__(self, brand, cpu, ram, gpu, price):
        super().__init__(brand, cpu, ram, gpu)
        self.price = price 
        
    def get_price(self):
        return f"{self.brand} Computer Price : {self.price}"

l = Laptop("Honor", "Intel Core i5 10.Generation", "8 GB DDr4", "Internal", 8500)
print(l.print_information)
print(l.get_price())
print()
d = Desktop("Assembled", "AMD Ryzen 5 2600", "16 GB DDr4", "RX 580 Sapphire Pulse 8 GB", 12500)
print(d.print_information)
print(d.get_price())