# Guy's object oriented (OOP) guide:

class Employee:  # Create a class | class 'class_name':
    emp_n = 0  # Class var
    def __init__(self,first,last,pay):  # Contstructor method, calls when an object is created.
        self.first = first  # 'self' represents the instance of the class.
        self.last = last
        self.email = first + '.' + last + '@pago-corp.com'
        self.pay = pay
        Employee.emp_n += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)


class Developers(Employee):
    dev_n = 0
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        Developers.dev_n += 1

class Managers(Employee):
    manager_emp = 0
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        Managers.manager_emp += 1

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        print(self.first,'\'s Employees :\n',sep='')
        for c,i in enumerate(self.employees,1):
            print(c,'. ',i.fullname(),sep='')



emp_1 = Employee('Betanir','Taggar',12500)
manager_1 = Managers('Guy','Taggar',37233)

manager_1.add_emp(emp_1)
manager_1.print_emps()
