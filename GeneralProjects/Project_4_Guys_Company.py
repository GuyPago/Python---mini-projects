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


# dev_1.fire()
# Employee.fire_rand()
# Employee.print_workers('all')




def panel():
    cls=Employee
    flag = True
    while flag:
        dict = {'d':dots,'h':panel_help,'l':cls.print_workers,'w':cls.print_salaries,
                'q':quit,'f':cls.fire}
        x=input('Hello to \'Pago-corp industries\' HR panel.  Enter \'h\' for help\n')
        if x in dict.keys():
            print(''); dict[x]()
        elif x=='c':
            cls=what_class()
        elif x=='q':
            break
        else:
            print('Error\nNot entered a valid value.\n')
