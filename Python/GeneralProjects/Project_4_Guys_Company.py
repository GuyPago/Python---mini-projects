# Guy's company project.
import operator
from data.Project_4_classes import *



dev_1 = Developer('Betanir','Taggar',12500,'C#')
manager_2 = Manager('Yulia','Kartsev',7500)
manager_1 = Manager('Ram','Taggar',27000,[dev_1])
emp_3 = Developer('Ido','Ashkenazi',11000,'java')
CEO_1 = CEO('Guy','Taggar',lv=100)
emp_2 = Employee('Test','Employee',1000,under=manager_2)
emp_4 = Employee('Yana','Lizrazon',5000,under=manager_2)
CEO_2 = CEO('Yaniv','Kenz')
# Employee.print_workers()
# Developer.print_workers()
# Manager.print_workers()
# manager_2.print_emps()
# CEO_1.print_emps()



# Employee.print_workers()
Employee.print_salaries()
manager_2.apply_raise(bonus=5400)
Employee.print_salaries()

manager_2.print_emps()
