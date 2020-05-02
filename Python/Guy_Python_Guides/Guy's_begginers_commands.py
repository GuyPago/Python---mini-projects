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


print('_'.join('Betanir')+'.')  # Put values between letters. | 'str'.join(var)

# List/set/tuple/dict

# List
cart = ["corn","milk","cheetos","milk"]  # Create a list. | 'list_name' = ['x','y','z']
cart[1] = 'popcorn'  # Change second item to 'popcorn' | 'list'[i] = 'x'
cart.append('potato')  # Add a new item to last. | 'list'.append('new_item')
cart.pop(2)  # Removes Third item | 'list'.pop(i) \ default == -1
cart.clear()  # Clears all items. | 'list'.clear()
empty_list = []  # Create an empty list. | 'list' = []
print(cart)

# Tuple - an immutable list.
cart_2 = ("corn","milk","cheetos")  # Create a tuple. | 'tuple_name' = ['x','y','z']
cart_2.index('milk')  # Returns the index of milk | 'list'.index('word')
empty_tuple = ()  # Create an empty tuple. | 'tuple' = ()
print(cart_2)  # Tuples are immutable(can't modify/add/remove items)

# Set - no index order, ignores duplicate values.
foods = {'water','milk','water'}  # Crate a set. | 'set_name' = {'x','y','z'}
foods = set(cart) # Convert a list into a set. | 'new_set' = set('list')
foods.add('coco') # Adds a single element to set. | 'set'.add('item')
foods.update(cart)  # Adds multiple elements to set. | 'set'.update('x','y','z')
foods.pop()  # Remove & return a random item. | 'set'.pop()
foods.clear()  # Clears all items. | 'list'.clear()
empty_set = set()  # Create an empty set. | 'set' = set()
print(foods)


# Create a dictionary  | 'dict_name' = {'key':'value','key':'value','key:value'}
dict_coding_lang = {'Guy':'Python', 'Betanir':'C#','Ram':'Pascal'}
dict_coding_lang['Yulia'] = "Nothing"  # Adds a dict item. | 'dict_name'['key'] = 'value'
print(dict_coding_lang)
print(dict_coding_lang['Ram'])  # Prints dictionary definition for 'Ram'.

dict_coding_lang.update({'Yulia':'HTML'})  # Updates value.
print(len(dict_coding_lang))  # Prints the length of the dictionary.

for k,v in dict_coding_lang.items():  # prints a list with dict keys and values.
    print(k + ': ' + v + ".")

# ^^^^^End^^^^^ #


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
