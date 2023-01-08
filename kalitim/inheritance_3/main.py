from management import Management
from engineers import Engineer
from janitor import Janitor
from print_info import Print

p = Print()

p.add(Engineer(1, "Mehmet", "Solak", 19, "Junior Full Stack Developer", 2018, 200, 35))
p.add(Management(2, "Alaettin", "Ucan", 40, "pow(Senior, Senior) * Full Stack Computer Engineer", 2003, 350, 50))
p.add(Janitor(3, "Kadir", "Akgun", 33, "Janitor", 2010, 150, 30))

p.print()
p.file_handling()