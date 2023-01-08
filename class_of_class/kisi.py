class Kisi:
    def __init__(self, isim, soyisim, yas):
        self._isim = isim 
        self._soyisim = soyisim 
        self._yas = yas 
        
    @property
    def isim(self):
        return self._isim 
    
    @property
    def soyisim(self):
        return self._soyisim
    
    @property
    def yas(self):
        return self._yas 