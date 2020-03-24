from IPython.display import Math

# Arithmetic progression

a1 = int(input("please enter 'a1': "))
d = int(input("Please enter 'd': "))
n = int(input("Please enter 'n': "))

an = a1 + (n-1)*d
Sn = (n/2)*(2*a1 + (n-1)*d)
Math(r'a_n~=~a_1+(n-1)d')  # 'an' function Algebric display
Math(r'S_n ~=~ \frac{n}{2} [2a_1+(n-1)d]')  # 'Sn' function Algebric display

print("a"+str(n)+" = " + str(an))  # Prints 'an'
print("s"+str(n)+" = " + str(Sn))  # Prints 'Sn'

# Geometric progression
a1 = int(input("please enter 'a1': "))
q = int(input("Please enter 'q': "))
n = int(input("Please enter 'n': "))

an = a1*q**(n-1)
Sn = (a1*(q**n - 1))/(q - 1)
print("a"+str(n)+" = " + str(an))  # Prints 'an'
print("s"+str(n)+" = " + str(Sn))  # Prints 'Sn'
