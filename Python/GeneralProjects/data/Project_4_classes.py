class Employee:
    raise_amount = 1.03
    staff = []

    def __init__(self,first,last,pay=20,lv=1,under=None):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@pago-corp.com'
        self.pay = pay
        self.lv = lv
        Employee.staff.append(self)
        try:
            under.employees.append(self)
        except :
            pass

    def __lt__(self,other):
        return self.lv < other.lv

    def fire(self):
        self.lv = 0

    @classmethod
    def print_emp_n(cls):
        n = len(list(filter(lambda x: x.lv !=0,cls.staff)))
        print('Pago-Corp is currently hiring {} {}s.'.format(n,cls.__name__))

    @classmethod
    def print_workers(cls,dimos=False):
        if dimos is True:
            former = ' former'
            emp_filter = lambda x: x.lv == 0
        else:
            former = ''
            emp_filter = lambda x: x.lv != 0

        print('Pago-Corp industries{} {}s: '.format(former,cls.__name__))
        for c, emp in enumerate(sorted(filter(emp_filter,cls.staff),reverse=True),1):
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

    def apply_raise(self,perc=0,bonus=0):
        if (perc == 0) and (bonus == 0):
            self.pay = int(self.pay * self.raise_amount)
        else:
            try:
                self.pay = int((self.pay + bonus) * (1 + perc/100))
            except TypeError:
                print('Error!\nRaise for {} failed!'.format(self.first)
                        + '\nNot entered a numeric value\n')

class Manager(Employee):
    staff = []
    raise_amount = 1.07

    def __init__(self,first,last,pay=400,employees=None,lv=5):
        super().__init__(first,last,pay,lv)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        self.staff.append(self)

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
    raise_amount = 1.1

    def __init__(self,first,last,pay=150000,lv=10,employees=Employee.staff):
        Employee.__init__(self,first, last, pay, lv)
        self.employees = [worker for worker in employees if worker.__class__.__name__ != 'CEO']
        self.staff.append(self)

class Developer(Employee):
    staff = []
    raise_amount = 1.06

    def __init__(self,first,last,pay,prog_lang=None,lv=3):
        super().__init__(first, last, pay, lv)
        self.prog_lang = prog_lang
        self.staff.append(self)
