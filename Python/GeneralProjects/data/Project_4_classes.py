from random import randint
import time
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
    def fire_rand(cls):
        if cls.__name__.startswith(('E','A','I','O','U')):
            a = 'an'
        else:
            a = 'a'
        emp = cls.staff[randint(0,len(cls.staff)-1)]
        i = 0
        print('Trying to fire {} {}..'.format(a,cls.__name__))
        time.sleep(1.5)
        while emp.lv >= 5 and i < 1000:
            emp = cls.staff[randint(0,len(cls.staff)-1)]
            i+=1
        if i == 1000:
            print('Failed!\nNo {} was fired, all have permanence.\n'.format(cls.__name__))
        else:
            emp.lv = 0
            print('Success!\n{} was fired.\n'.format(emp.fullname))

    @classmethod
    def print_emp_n(cls):
        n = len(list(filter(lambda x: x.lv !=0,cls.staff)))
        print('Pago-Corp is currently hiring {} {}s.'.format(n,cls.__name__))

    @classmethod
    def print_workers(cls,dimus=False):
        former,emp_filter = cls.is_worker(dimus)

        print('Pago-Corp industries {}{}s: '.format(former,cls.__name__))
        for c, emp in enumerate(sorted(filter(emp_filter,cls.staff),reverse=True),1):
            print(c, '. ', emp.fullname,' - ',emp.__class__.__name__ ,sep='')
        print('\n')

    @classmethod
    def print_salaries(cls,dimus=False):
        former,emp_filter = cls.is_worker(dimus)

        print('Pago-Corp industries salaries for {}{}s: '.format(former,cls.__name__))
        for emp in sorted(filter(emp_filter,cls.staff),key=lambda x: x.pay, reverse=True):
            print(emp.fullname,'-',emp.pay)
        print('\n')

    @staticmethod
    def is_worker(dimus):
        if dimus is True:
                former = 'former '
                emp_filter = lambda x: x.lv == 0
        elif dimus is False:
                former = ''
                emp_filter = lambda x: x.lv != 0
        elif dimus == 'all':
                former = '(current & former) '
                emp_filter = None
        else:
            raise ValueError('dimus must be True,False, or \'all\'')

        return former,emp_filter

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self,perc=0,bonus=0):
        if (perc == 0) and (bonus == 0):
            self.pay = int(self.pay * self.raise_amount)
        else:
            try:
                self.pay = int(self.pay * (1 + perc/100) + bonus)
            except TypeError:
                print('Error!\nRaise for {} failed!'.format(self.first)
                        + '\nNot entered a numeric value\n')

class Developer(Employee):
    staff = []
    raise_amount = 1.06

    def __init__(self,first,last,pay,prog_lang=None,lv=3):
        super().__init__(first, last, pay, lv)
        self.prog_lang = prog_lang
        self.staff.append(self)

class Manager(Developer):
    staff = []
    raise_amount = 1.07

    def __init__(self,first,last,pay=1000,prog_lang=None,employees=None,lv=5):
        super().__init__(first,last,pay,prog_lang,lv)
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
            employees = [i for i in Employee.staff if i.__class__.__name__!='CEO' and i.lv!=0]
            print(self.first,'\'s Employees :',sep='')
            for c,i in enumerate(employees,1):
                print('{}. {} - {}'.format(c,i.fullname(),i.__class__.__name__))
            print('\n')
        elif len(list(filter(lambda x: x.lv!=0,self.employees))) == 0:
            print('{} doesn\'t have employees.\n'.format(self.first))
        else:
            print(self.first,'\'s Employees :',sep='')
            for c,i in enumerate(list(filter(lambda x: x.lv!=0,self.employees)),1):
                print(c,'. ',i.fullname(),sep='')
            print('\n')

class CEO(Manager):
    staff = []
    raise_amount = 1.1

    def __init__(self,first,last,pay=150000,lv=10,employees=Employee.staff):
        Employee.__init__(self,first, last, pay, lv)
        self.employees = [worker for worker in employees if worker.__class__.__name__ != 'CEO']
        self.staff.append(self)
