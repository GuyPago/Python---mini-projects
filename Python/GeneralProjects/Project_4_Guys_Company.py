# Guy's company project.
import operator
from data.Project_4_classes import *



dev_1 = Developer('Betanir','Taggar',12500,'C#')
manager_2 = Manager('Yulia','Kartsev',7500)
manager_1 = Manager('Ram','Taggar',27000,employees=[dev_1])
dev_2 = Developer('Ido','Ashkenazi',11000,'java')
CEO_1 = CEO('Guy','Taggar',lv=15)
emp_1 = Employee('Test','Employee',1000,under=manager_2)
emp_2 = Employee('Yana','Lizrazon',5000,under=manager_2)
CEO_2 = CEO('Yaniv','Kenz')




dev_1.apply_raise(70,700000)
Employee.print_workers()
Developer.fire_rand()
Employee.fire_rand()
Employee.print_workers()
dev_1.lv = 6
