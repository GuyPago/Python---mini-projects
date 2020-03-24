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
first3letters = greet[0:4]  # Stores the x to y letters of the string. | [x:y]
#  Using [-x,-y] counts [x,y] letters from the end.
print("Your name's first letter is: " + firstLetter)
print("Hitler is in " + first3letters)

num = 25
favoriteNumber = "Your favorite number is: "
print(favoriteNumber + str(num))  # Turns a variable to string. | (str)
print(len(favoriteNumber))  # prints the length of the string. | (len)

test = "It is a test."
test = test.replace("is", "was")  # Replaces x with y | 'var'.replace("x", "y")
print(test)

print("Lets count to 10 :")
count = 0
while count < 10:  # While loop | while 'condition':
    count = count + 1
    print(count)


# Functions

def welcomeUser(name):  # defines a function | def 'funcName'(parameter)
    print("Welcome, " + name + "!")
welcomeUser("Betanir")  # call function + parameter


def toFahrenheit(celsius):
    f = celsius * 9/5 + 32
    return f  # returns a value | return 'value'

degreesInput = input("Enter celsius degrees: ")
degrees = toFahrenheit(int(degreesInput))
print(degreesInput + " degrees celsius are " + str(degrees) + " degrees Fahrenheit")
