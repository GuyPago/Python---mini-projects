import math
import draft

n = 1
e = 1/math.factorial(n)

while n < 19:
    print(e)
    n = n+1
    e = e + e

draft.say_my_name()
