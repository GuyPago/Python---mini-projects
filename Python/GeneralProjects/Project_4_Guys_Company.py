# Guy's company project.
from data.Project_4_classes import *



dev_1 = Developer('Betanir','Taggar',12500,'C#')
manager_2 = Manager('Yulia','Kartsev',7500)
manager_1 = Manager('Ram','Taggar',27000,employees=[dev_1])
dev_2 = Developer('Ido','Ashkenazi',11000,'java')
CEO_1 = CEO('Guy','Taggar',lv=15)
emp_1 = Employee('Test','Employee',1000,under=manager_2)
emp_2 = Employee('Yana','Lizrazon',5000,under=manager_2)
CEO_2 = CEO('Yaniv','Kenz')




dev_1.apply_raise(70,5000)
Employee.print_workers()
# Developer.fire_rand()
# print(CEO_1.hire_date)
# print(CEO_2.hire_date)
# print(CEO_1.hire_date < CEO_2.hire_date)
manager_1.fire()
time.sleep(2)
CEO_2.fire()
time.sleep(1)
Developer.fire_rand()
# Developer.fire_rand()
# Employee.fire_rand()
# Employee.print_workers()
# CEO_1.fire()
Employee.print_workers()
Employee.print_workers(dimus='all')
# print(manager_1.fire_date)
