# Convert Integer input to 'Binary' language.
def int_to_binary(val=0):
    return bin(val)[2:].zfill(8)  # Prints from the 2nd letter | Prints min of 8 letters.

for i in range(100):  # Prints binary values of 0 to 100.
    print(int_to_binary(i))
# ^^^^^End^^^^^ #

# Convert user input to 'ASCII' language.
while True:
    user_input = input("enter any key to print(enter 'q' to quit):\n") or "0"  # '0' is default input.
    if user_input == "q":
        print("ending program...bye!\n\n\n")
        break  # Break/end the loop.
    else:
        print("user input was",user_input)
        print("the value of",user_input,"in ASCII is",str(ord(user_input)),"\n\n\n")
# ^^^^^End^^^^^ #

# Caesar cipher. | ROT13 algorithm.
str = 'Hey, how are you today?'
str_2 = ''
for i in str:
    str_2+= chr(ord(i)+13)
print(str_2)
# ^^^^^End^^^^^ #


# Print the ABC.
import string
ABC = []
for i in string.ascii_lowercase:
    ABC += i
print(ABC)
# Or
abc = list(string.ascii_lowercase)
# Or not by list:
acb = string.ascii_lowercase
print(', '.join(acb))
# ^^^^^End^^^^^ #

# Swap values.
t = 10
u = 5

t,u = u,t
print("t =",t)
print("u =",u)
# ^^^^^End^^^^^ #


# Backward list/string/tuple/set.
nir = 'Betanir'
nir_back = nir[::-1]
print(nir_back)

nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::-1])
# ^^^^^End^^^^^ #


#  Multiplication table
x = 10
y = 10

for i in range(1, y+1):   # set a range of numbers | range('start','end','jump')
    for j in range(1, x+1):  # range always stops at (n-1). | range(0, n)
        print(i * j, "\t",end="")  # set a 'tab' spacing. | '\t'
    print()  # line break at the end of the loop.
# ^^^^^End^^^^^ #


#  Change every list number
def multiply(numbers):
    ns = []  # Creates an empty list.
    for i in numbers:
        ns.append(i * 2)  # add item 'i' to end of list. | 'list_name'.append(i)
    print(ns)

list = [1,4,5,2,3,4,1]
multiply(list)

# ^^^^^End^^^^^ #


# Recursion - call a function in itself.  --> Factorial function:
def factorial(n):
    assert n>=0, 'Value must be positive' # Demand n >=0, if false, raise error.
    assert round(n)==n, 'Value must be integer'
    if (n == 1) | (n == 0):  # '|' == 'or'
        return 1
    else:
        return n * factorial(n-1)  #  Recursion.

number = factorial(5)
print(number)
# ^^^^^End^^^^^ #


# Recursion. | Call a function in itself for a set or inf amount of time.
def recursive_func(x):
    print(x)
    if (x > 0):
        recursive_func(x - 1)

print(recursive_func(10))
# ^^^^^End^^^^^ #


# Map - perform a function to every list item. | Returns an iterable.
def add_five(x):
    return x+5

nums = [1,2,3,4,5,6,7,8,9,10]
nums = list(map(add_five,nums))  # map('func','list') | returns an iterable, so
# we need to convert it to list.

# Or by lambda function:
nums = list(map(lambda x: x+5,nums))

# This specific example can be doen by list comprehension:
nums = [x+5 for x in nums]
print(nums)
# ^^^^^End^^^^^ #


# Filter - remove items that don't match a predicate. | Returns an iterable.
def is_even(x):
    return x%2 == 0
nums = [1,2,3,4,5,6,7,8,9,10]
nums = list(filter(is_even,nums))  # filter('func','list') | returns an iterable
# so we need to convert it to list.

#or by lambda function:
nums = list(filter(lambda x: x%2 == 0,nums))
print(nums)
# This specific example can be doen by list comprehension:
nums = [x for x in nums if x%2 ==0]
# ^^^^^End^^^^^ #


# Specific letter counter. | count(world,'requested letter')
def count(word,L):
    c = 0
    for i in word:
        if L == i:
            c+=1
    return c
count('abba','b')

# Return letters as % of text.
with open('text.txt', 'r') as f:
    text = f.read()
total = 0

for char in string.ascii_letters + '0123456789':  #  A-Z + a-z + 0-9
    percent = 100* count(text,char)/len(text)
    if (percent > 0):
        print('{} - {}%'.format(char,round(percent, 2)))
        total += percent
    else:
        continue
print(round(total,2))  # rounds number to 2 figures after '.' | round('number','figures')
# ^^^^^End^^^^^ #
