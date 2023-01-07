from hourlypersonnel import HourlyPersonnel
from manager import Manager
from print import Print 

p = Print()

p.add(Manager("Mehmet", "SOLAK", 112334555, 7500, "Mersin", "Akdeniz"))
p.add(HourlyPersonnel("Mustafa", "AKIPEK", 555433211, 150, 36, "Bursa", "Gemlik"))
p.print()