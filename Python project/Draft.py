import cmath
cmath.sqrt(4)
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/2*a
x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/2*a
print(x1.real)
if x1 == x1.real:
    x1 = int(x1.real)
if x2 == int(x2):
    x2 = int(x2)

if x1 == x2:
    print("\nx = " + str(x1))
else:
    print("\nAnswers are:\n" + "x1 = " + str(x1) + "\n" + "x2 = " + str(x2))
