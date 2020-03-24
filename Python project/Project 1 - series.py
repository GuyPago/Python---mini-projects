# Arithmetic progression
print("סדרה חשבונית")
a1 = int(input("please enter 'a1': "))
d = int(input("Please enter 'd': "))
n = int(input("Please enter 'n': "))

an = a1 + (n-1)*d
print("a"+str(n)+" = " + str(an))

# Geometric progression
a1 = int(input("please enter 'a1': "))
q = int(input("Please enter 'q': "))
n = int(input("Please enter 'n': "))

an = a1*q**(n-1)

print("a"+str(n)+" = " + str(an))
