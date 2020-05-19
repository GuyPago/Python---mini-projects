# Guy's company project.
import operator
from data.Project_4_classes import *



dev_1 = Developer('Betanir','Taggar',12500,'C#')
manager_2 = Manager('Yulia','Kartsev',7500)
manager_1 = Manager('Ram','Taggar',27000,[dev_1])
dev_2 = Developer('Ido','Ashkenazi',11000,'java')
CEO_1 = CEO('Guy','Taggar',lv=100)
emp_1 = Employee('Test','Employee',1000,under=manager_2)
emp_2 = Employee('Yana','Lizrazon',5000,under=manager_2)
CEO_2 = CEO('Yaniv','Kenz')



print('Employees = {}'.format(Employee.emp_n))
Developer.print_workers()
print(Developer.emp_n)
print(Employee.emp_n)
dev_1.fire()
print(Developer.emp_n)
print(Employee.emp_n)
Developer.print_workers()
CEO.print_emp_num()
