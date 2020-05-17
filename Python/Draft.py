# # OOP
#
# class employee:
#
#     emp_n = 0
#     def __init__(self,first,last,age):
#         self.first = first
#         self.last = last
#         self.age = age
#         self.full = first + ' ' + last
#
#     def fire_emp():
#         pass
#
#         employee.emp_n += 1
#     def fullname(self):
#         return self.first + ' ' + self.last
#
#
# # emp_1 = employee('Guy','Taggar',25)
# # emp_2 = employee('Yulia','Kartsev',22)
# # emp_3 = employee('Betanir','Taggar',21)
#
#
# class bugs:
#     bugs_n = 0
#     eyes = 2
#     def __init__(self,size,legs):
#         self.legs = legs
#         self.size = size
#         bugs.bugs_n += 1
#
#     @classmethod
#     def set_eyes(cls,new_eyes):
#         cls.eyes = new_eyes
#
#     @classmethod
#     def new_bug(cls,bug_str):
#         size,legs = bug_str.split('-')
#         return cls(size,legs)
#
# kiki = bugs(12,3)
# print(kiki.size)
# print(bugs.bugs_n)
# botten = bugs.new_bug('4-3')
#
#
#
# class combine:
#     def __init__(self,word):
#         self.word = word
#
#     def __truediv__(self,other):
#         line = '=' * len(other.word)
#         return '\n'.join([self.word + ',\n',line,other.word,line])
#
# hi = combine('Hello')
# beta = combine('Mr, Betanir.')
# print(hi/beta)
#
# def beta(name,age,wage):
#     assert (age > 18),'You are too young'
#     print('Welcome, {}, how are you today ?'.format(name))
#
# beta('Guy',25,5555)


print('hey')
x = 7
y = 5



print(x+y)
x = 4
print(x+y)
