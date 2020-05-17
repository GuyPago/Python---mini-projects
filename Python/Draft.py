# OOP

class employee:

    emp_n = 0
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        self.full = first + ' ' + last

    def fire_emp():
        pass

        employee.emp_n += 1
    def fullname(self):
        return self.first + ' ' + self.last


# emp_1 = employee('Guy','Taggar',25)
# emp_2 = employee('Yulia','Kartsev',22)
# emp_3 = employee('Betanir','Taggar',21)


class bugs:
    bugs_n = 0
    eyes = 2
    def __init__(self,size,legs):
        self.legs = legs
        self.size = size
        bugs.bugs_n += 1

    @classmethod
    def set_eyes(cls,new_eyes):
        cls.eyes = new_eyes

    @classmethod
    def new_bug(cls,bug_str):
        size,legs = bug_str.split('-')
        return cls(size,legs)

kiki = bugs(12,3)
print(kiki.size)
print(bugs.bugs_n)
botten = bugs.new_bug('4-3')



class combine:
    def __init__(self,word):
        self.word = word

    def __truediv__(self,other):
        line = '=' * len(other.word)
        return '\n'.join([self.word + ',\n',line,other.word,line])

hi = combine('Hello')
beta = combine('Mr, Betanir.')
print(hi/beta)

def beta(name,age,wage):
    assert (age > 18),'You are too young'
    print('Welcome, {}, how are you today ?'.format(name))

beta('Guy',25,5555)



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
