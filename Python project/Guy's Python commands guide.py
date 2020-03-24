greet = "Hello, "  # var | x = "y"
name = input("What's Your name? ")
greetName = greet + name + ". "
# Adds a line break ("\n") || Prints x times (*x)
print((greetName + "\n") * 2)

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

count = 1
while count < 10:  # While loop | while 'condition':
    count = count + 1
    print(count)
