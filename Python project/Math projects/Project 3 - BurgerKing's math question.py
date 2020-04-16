import math

# Burger-king's free woopher math question. Done by 2 different methods.
def method_1():
    n = 1
    Sum = 0
    while(n <= 461):
        solve = (-1)*((-1)**n * ((math.factorial(5)*5)/math.factorial(4))**(1/2))
        Sum += solve
        n += 1
    return Sum


def method_2():
    n = 1
    Sum = []
    while (n <= 461):
        solve = (-1)*((-1)**n * ((math.factorial(5)*5)/math.factorial(4))**(1/2))
        Sum.append(solve)
        n += 1
    return sum(Sum)


print(method_1() == method_2())
