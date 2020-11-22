''' Exercise #1. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
name  = 'Guy' # Replace ??? with a string of your choice.
# Write the rest of the code for question 1 below here.
print('Hello ' + name + '!')


#########################################
# Question 2a - do not delete this comment
#########################################
my_str2a = 'Betanir' # Replace ??? with a string of your choice.
# Write the rest of the code for question 2a below here.
print(len(my_str2a))


#########################################
# Question 2b - do not delete this comment
#########################################
my_str2b = 'This,,,, is, a test, yes.' # Replace ??? with a string of your choice.
# Write the rest of the code for question 2b below here.
print(len(my_str2b)-my_str2b.count(','))


#########################################
# Question 3 - do not delete this comment
#########################################
my_str3 = 'A significant test by Guy' # Replace ??? with a string of your choice.
# Write the rest of the code for question 3 below here.
middle = int(len(my_str3)/2)
print(str.upper(my_str3)[:middle] + ':' + str.lower(my_str3)[middle:])


#########################################
# Question 4 - do not delete this comment
#########################################
R  = 6.0 # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 4 below here.
pi = 3.14
D = 2*R
C = 2*pi*R
A = pi*R**2

print('Size of circle diameter is:', D)
print('Circumference is:', C)
print('Area is:', A)

#########################################
# Question 5 - do not delete this comment
#########################################
repeats = 3 # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 4 below here.
x = 'I will never copy homework\n'
print(x * repeats)
