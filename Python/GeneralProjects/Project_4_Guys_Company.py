# Guy's company project.
import operator
class Employee:
    raise_amount = 1.03
    staff = []
    emp_n = 0

    def __init__(self,first,last,pay=20,lv=1,under=None):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@pago-corp.com'
        self.pay = pay
        self.lv = lv
        Employee.emp_n += 1
        Employee.staff.append(self)
        try:
            under.employees.append(self)
        except :
            pass

    def __lt__(self,other):
        return self.lv < other.lv


    @classmethod
    def print_workers(cls):

        print('Pago-Corp industries {}s: '.format(cls.__name__))
        for c, emp in enumerate(sorted(cls.staff,reverse=True),1):
            print(c, '. ', emp.fullname(),' - ',emp.__class__.__name__ ,sep='')
        print('\n')

    @classmethod
    def print_salaries(cls):
        print('Pago-Corp industries salaries for {}s: '.format(cls.__name__))
        for emp in sorted(cls.staff,key=lambda x: x.pay, reverse=True):
            print(emp.fullname(),'-',emp.pay)
        print('\n')

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Manager(Employee):
    staff = []
    emp_n = 0
    raise_amount = 1.1
    def __init__(self,first,last,pay=400,employees=None,lv=5):
        super().__init__(first,last,pay,lv)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        self.staff.append(self)
        Manager.emp_n += 1

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        if self.__class__.__name__ == 'CEO':
            employees = [i for i in Employee.staff if i.__class__.__name__!='CEO']
            print(self.first,'\'s Employees :',sep='')
            for c,i in enumerate(employees,1):
                print(c,'. ',i.fullname(),sep='')
            print('\n')
        else:
            print(self.first,'\'s Employees :',sep='')
            for c,i in enumerate(self.employees,1):
                print(c,'. ',i.fullname(),sep='')
            print('\n')

class CEO(Manager):
    staff = []
    emp_n = 0
    def __init__(self,first,last,pay=150000,lv=10,employees=Employee.staff):
        Employee.__init__(self,first, last, pay, lv)
        self.employees = [worker for worker in employees if worker.__class__.__name__ != 'CEO']
        self.staff.append(self)
        CEO.emp_n += 1

class Developer(Employee):
    staff = []
    emp_n = 0
    raise_amount = 1.06

    def __init__(self,first,last,pay,prog_lang=None,lv=3):
        super().__init__(first, last, pay, lv)
        self.prog_lang = prog_lang
        self.staff.append(self)
        Developer.emp_n+=1




dev_1 = Developer('Betanir','Taggar',12500,'C#')
emp_1 = Employee('Yulia','Kartsev',7500)
manager_1 = Manager('Ram','Taggar',27000,[dev_1,emp_1])
emp_3 = Developer('Ido','Ashkenazi',11000,'java')
CEO_1 = CEO('Guy','Taggar',lv=100)
emp_2 = Employee('Test','Employee',1000,under=manager_1)
CEO_2 = CEO('Yaniv','Kenz')
# Employee.print_workers()
# Developer.print_workers()
# Manager.print_workers()
# manager_2.print_emps()
# CEO_1.print_emps()



Employee.print_workers()
Employee.print_salaries()
emp_1.apply_raise()
Employee.print_salaries()
emp_1.apply_raise()
Employee.print_salaries()
