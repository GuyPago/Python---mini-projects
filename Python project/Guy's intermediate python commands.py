
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

# Factorial algorithm.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)  # call a function inside itself.

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
