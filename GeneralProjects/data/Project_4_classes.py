from random import randint
import datetime
import time
import sys,inspect




class Employee:
    raise_amount = 1.03
    staff = []
    i = 1

    def __init__(self,first,last,pay=20,lv=1,under=None):
        self.id = Employee.i
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@pago-corp.com'
        self.pay = pay
        self.lv = lv
        self.hire_date = datetime.datetime.now()
        self.fire_date = None
        Employee.staff.append(self)
        Employee.i += 1
        try:
            under.employees.append(self)
        except :
            pass

    def __lt__(self,other):
        return self.lv < other.lv

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def fire(self):
        self.lv = 0
        self.fire_date = datetime.datetime.now()
        print('{} was fired.\n'.format(self.fullname))

    def apply_raise(self,perc=0,bonus=0):
        print('Giving {} a raise'.format(self.fullname),end='')
        dots()
        if (perc == 0) and (bonus == 0):
            perc = (self.raise_amount-1)*100
        #     self.pay = int(self.pay * self.raise_amount)
        # else:
        try:
            old_pay = self.pay
            self.pay = int(self.pay * (1 + perc/100) + bonus)
            print('\nSuccess !\n{}\'s salary was set from {} to {}.\n'
                                       .format(self.first,old_pay,self.pay))
        except TypeError:
            print('\nError!\nRaise for {} failed - '.format(self.first)
                    + 'not entered a valid raise value.\n')
    @classmethod
    def fire_rand(cls):
        print('Trying to fire a random {}'.format(cls.__name__),end='',flush=True)
        dots()
        pool = list(filter(lambda x: x.lv!=0,cls.staff))
        try:
            emp = pool[randint(0,len(pool)-1)]
        except ValueError:
            print('Failed!\nThere are no {}s in Pago-Corp\n'.format(cls.__name__))
            return None
        i = 0
        while emp.lv >= 5 and i < 1000:
            emp = pool[randint(0,len(pool)-1)]
            i+=1
        if i == 1000:
            print('Failed!\nNo {} was fired, all have permanence.\n'
                                                          .format(cls.__name__))
        else:
            print('\nSuccess!')
            emp.fire()

    @classmethod
    def print_emp_n(cls):
        n = len(list(filter(lambda x: x.lv !=0,cls.staff)))
        print('Pago-Corp is currently hiring {} {}s.'.format(n,cls.__name__))

    @classmethod
    def print_workers(cls,dimus=False):
        former,emp_filter = cls.is_worker(dimus)

        print('Pago-Corp industries {}{}s: '.format(former,cls.__name__))
        for c, emp in enumerate(sorted(filter(emp_filter,cls.staff),
                               key=lambda x:(x.lv,x.fire_date),reverse=True),1):
            if emp.fire_date is None:
                print('{}. {} - {}'.format(c,emp.fullname,emp.__class__.__name__))
            else:
                print('{}. {} - {},  unemployment date -> [{} at {}]'
                    .format(c,emp.fullname,emp.__class__.__name__,emp.fire_date
                                  .strftime('%x'),emp.fire_date.strftime('%X')))
        print('\n')

    @classmethod
    def print_salaries(cls,dimus=False):
        former,emp_filter = cls.is_worker(dimus)

        print('Pago-Corp industries salaries for {}{}s: '
                                                   .format(former,cls.__name__))
        for emp in sorted(filter(emp_filter,cls.staff),
                                             key=lambda x: x.pay, reverse=True):
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

class Developer(Employee):
    staff = []
    raise_amount = 1.06

    def __init__(self,first,last,pay,prog_lang=None,lv=3,id=0):
        super().__init__(first, last, pay, lv,id)
        self.prog_lang = prog_lang
        self.staff.append(self)

class Manager(Developer):
    staff = []
    raise_amount = 1.07

    def __init__(self,first,last,pay=1000,prog_lang=None,employees=None,lv=4):
        super().__init__(first,last,pay,prog_lang,lv,id)
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
            employees = [i for i in Employee.staff if
                                        i.__class__.__name__!='CEO' and i.lv!=0]

            print(self.first,'\'s Employees :',sep='')
            for c,i in enumerate(employees,1):
                print('{}. {} - {}'.format(c,i.fullname,i.__class__.__name__))
            print('\n')
        elif len(list(filter(lambda x: x.lv!=0,self.employees))) == 0:
            print('{} doesn\'t have employees.\n'.format(self.first))
        else:
            print(self.first,'\'s Employees :',sep='')
            for c,i in enumerate(list(filter(lambda x: x.lv!=0,self.employees)),1):
                print(c,'. ',i.fullname,sep='')
            print('\n')

class CEO(Manager):
    staff = []
    raise_amount = 1.1

    def __init__(self,first,last,pay=150000,lv=10,employees=Employee.staff):
        Employee.__init__(self,first, last, pay, lv, id)
        self.employees = [worker for worker in employees if
                                            worker.__class__.__name__ != 'CEO']
        self.staff.append(self)





# Useful functions:
emp_types = inspect.getmembers(sys.modules[__name__], inspect.isclass)


def dots(dot=3,t=0.5):
    for i in range(dot):
        print('.',end='',flush=True)
        time.sleep(t)

def what_class():
    dict2={}
    print('What class?')
    for i,v in enumerate(emp_types,1):
        dict2[i] = v[1]
        print(i,'. ',v[0],'s',sep='')
    c = int(input('') or 3)
    return dict2[c]


def panel_help():
    print("""Navigation:
'c' -> Choose worker department (default = All)
'l' -> Print labor force.
'w' -> Print wages.
'f' -> Fire a worker.
'q' -> Quit.

    """)
