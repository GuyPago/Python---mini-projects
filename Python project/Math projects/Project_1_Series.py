from IPython.display import Math
import time

# Series algebric display:
Math(r'a_n~=~a_1+(n-1)d')  # 'an' function Algebric display
Math(r'S_n ~=~ \frac{n}{2} [2a_1+(n-1)d]')  # 'Sn' function Algebric display


# Arithmetic progression
def arithmetic_progression():
    while True:
        print("Welcome to Guy's geometric progression solver.   (enter 'q' to quit)\n")

        a1 = input("please enter 'a1': ")
        if (a1 == 'q'):
            print("Going back to hub..\n")
            time.sleep(2)
            break
        while type(a1) == str:
            try:
                a1 = float(a1)
                break
            except ValueError:
                print("Not entered any number\n")
                a1 = input("please enter 'a1': ")

        d_not_legit = True
        while d_not_legit:
            try:
                d = float(input("Please enter 'd': "))
                d_not_legit = False
            except ValueError:
                print("Not entered any number\n")
        n_not_legit = True
        while n_not_legit:
            try:
                n = int(input("Please enter 'n': "))
                n_not_legit = False
            except ValueError:
                print("Not entered any number\n")

        an = a1 + (n-1)*d
        Sn = (n/2)*(2*a1 + (n-1)*d)
        print("\nAnswers:\na"+str(n)+" = " + str(an))  # Prints 'an'
        print("s"+str(n)+" = " + str(Sn))  # Prints 'Sn'
        print("\n")

# Geometric progression
def geometric_progression():
    while True:
        print("Welcome to Guy's geometric progression solver.   (enter 'q' to quit)\n")

        a1 = input("please enter 'a1': ")
        if (a1 == 'q'):
            print("Going back to hub..\n")
            time.sleep(2)
            break
        while type(a1) == str:
            try:
                a1 = float(a1)
                break
            except ValueError:
                print("Not entered any number\n")
                a1 = input("please enter 'a1': ")

        q_not_legit = True
        while q_not_legit:
            try:
                q = float(input("Please enter 'q': "))
                q_not_legit = False
            except ValueError:
                print("Not entered any number\n")
        n_not_legit = True
        while n_not_legit:
            try:
                n = int(input("Please enter 'n': "))
                n_not_legit = False
            except ValueError:
                print("Not entered any number\n")

        an = a1*q**(n-1)
        Sn = (a1*(q**n - 1))/(q - 1)
        print("\nAnswers:\na"+str(n)+" = " + str(an))  # Prints 'an'
        print("s"+str(n)+" = " + str(Sn))  # Prints 'Sn'
        print("\n")
