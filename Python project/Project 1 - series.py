# Arithmetic progression

a1 = int(input("please enter 'a1': "))
d = int(input("Please enter 'd': "))
n = int(input("Please enter 'n': "))

an = a1 + (n-1)*d
Sn = (n/2)*(2*a1 + (n-1)*d)

print("a"+str(n)+" = " + str(an))  # Prints 'an'
print("s"+str(n)+" = " + str(Sn))  # Prints 'Sn'

# Geometric progression
a1 = int(input("please enter 'a1': "))
q = int(input("Please enter 'q': "))
n = int(input("Please enter 'n': "))

an = a1*q**(n-1)

print("a"+str(n)+" = " + str(an))  # Prints 'an'
print("s"+str(n)+" = " + str(Sn))  # Prints 'Sn'
