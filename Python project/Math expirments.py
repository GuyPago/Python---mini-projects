import math
math.sqrt(2)

Guy = "me"

# Recursion. | Call a function in itself for a set or inf amount of time.
def recursion_func(x):
    print(x)
    if (x > 0):
        recursion_func(x - 1)

print(recursion_func(10))

#  Multiplication table
x = 10
y = 10

for i in range(1, y+1):   # set a range of numbers | range('start','end','jump')
    for j in range(1, x+1):  # range always stops at (n-1). | range(0, n)
        print(i * j, "\t",end="")  # set a 'tab' spacing. | '\t'
    print()  # line break at the end of the loop.

# ^^^^^End^^^^^ #
