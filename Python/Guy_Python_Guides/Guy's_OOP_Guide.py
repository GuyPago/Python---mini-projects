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

class Vector3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __truediv__(self,other):
        return Vector3D(self.x/other.x, self.y/other.y, self.z/other.z)

    @classmethod
    def vector_str(cls,string):
        x,y,z = string.split('-')
        try:
            return cls(float(x),float(y),float(z))
        except ValueError:
            print('Error!\nvalues must be numbers')


d = Vector3D.vector_str('5-7-2')
a = Vector3D(2,3,4)
b = Vector3D(8,6,8)
c = b/a

f = Vector3D.vector_str('5-2-4')



# class Vector2D:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __sub__(self,other):
#         return Vector2D(self.x - other.x, self.y - other.y)
#
# first = Vector2D(5,2)
# second = Vector2D(2,4)
# result = first - second
# print(result.x,result.y,sep = '   ')
