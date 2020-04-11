import math

n = 1
e = 1/math.factorial(n)

while n < 19:
    print(e)
    n = n+1
    e = e + e


number = 5
while number < 10:
    print(number)
    number += 1


def first_func(bitc):
    print("You have",bitc*3637,"Dollars !")

bitcoin = 10
first_func(bitcoin)


def sec_func(int):
    return int * 2
sec = sec_func(4)


def thrd_func(trd):
    return trd // 2

thrd = thrd_func(sec)
thrd


def first_func(num=0):
    return num * 2

first_func()


def f(x=0):
    return x**2 + 2*x + 5

y = f(7)
y
