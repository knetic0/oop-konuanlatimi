from emp import FullTimeEmployee
from emp2 import HourlyEmployee
from payroll import Payroll

payroll = Payroll()

payroll.add(FullTimeEmployee('John', 'Doe', 6000))
payroll.add(HourlyEmployee('Jenifer', 'Smith', 200, 50))

payroll.print()