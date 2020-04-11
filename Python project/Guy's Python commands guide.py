greet = "Hello, "  # var | x = "y"
name = input("What's Your name? ")  # var gets input from user. | input("ask user")
greetName = greet + name + ". "
print((greetName + "\n") * 2)  # Adds a line break ("\n") || Prints x times (*x)

story = name + """ Has quite an interesting story,
He was just about to share it but \
suddenly, He turned into a frog. \n"""
#  Makes every natural lineBreak work | ("""x""") || Prevent a br by using (\)
print(story)

firstLetter = name[0]  # Gets the x letter of the string. | [x]
firstLetters = greet[0:4]  # Stores the x to y letters of the string. | [x:y]
#  Using [-x,-y] counts [x,y] letters from the end.
print("Your name's first letter is: " + firstLetter)
print("Hitler is in " + firstLetters)

num = 25
favoriteNumber = "Your favorite number is: "
print(favoriteNumber + str(num))  # Turns a variable to string. | (str)
print(len(favoriteNumber))  # prints the length of the string. | (len)

test = "It is a test."
test = test.replace("is", "was")  # Replaces x with y | 'var'.replace("x", "y")
print(test)

cart = ["corn","milk","cheetos"]  # Create a list. | 'list_name' = ['x','y','z']
print(cart)

foods = {'water','milk','water'}  # Crate a set.  | 'set_name' = {'x','y','z'}
print(foods)  # Sets ignore duplicate values.

# loops

print("Lets count to 10 :")
count = 0
while count < 10:  # While loop | while 'condition':
    count += 1
    print(count)

cart = ["corn","milk","cheetos"]
for i in cart:  # Print every list item. i starts at 0. | for i in 'list':
    print(i)

# Functions


def f(x=0):  # defines a function | def 'func_name'(parameter='default_value')
    return x**2 + 2*x + 5  # returns a value | return 'value'

y = f(7)  # Defines 'y' while x = 7
print(y)


def calc(*args):  # Allows multi parameter input. | 'func_name'(*args):
    total = 0
    for i in args:
        total += i
    print(total)  # Prints the sum of the multi-parameter input.

calc(1,36,4,51,6,7,6,50,4,3,2)


def welcomeUser(name="a"):
    print("Welcome, " + name + "!")
welcomeUser("Betanir")  # call function + parameter


def toFahrenheit(celsius):
    f = celsius * 9/5 + 32
    return f  # returns a value | return 'value'

degreesInput = input("Enter celsius degrees: ")
degrees = toFahrenheit(int(degreesInput))
print(degreesInput + " degrees celsius are " + str(degrees)
                   + " degrees Fahrenheit")  # continuation line break
