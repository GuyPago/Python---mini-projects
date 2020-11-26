''' Exercise #2. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
number = int(input('Enter a number:\n'))  # Replace ??? with an appropriate command to get a number from the user.
# Write the rest of the code for question 1 below here.
if number % 3 == 0:
    print('I am' ,number, 'and I am a multiplication of 3')
else:
    print('I am',number, 'and I am not a multiplication of 3')



#########################################
# Question 2 - do not delete this comment
#########################################
number = int(input('Enter a number:\n'))  # Replace ??? with an appropriate command to get a number from the user.
# Write the rest of the code for question 2 below here.
if number % 2 == 0:
    print('Even number')
if (number % 3 == 0) and (number % 6 != 0):  # Could use elif instead because if its divisible by 3 but not divisible by 6, it surely isnt divisible by 2.
    print('Divisible by 3')
if len(str(number)) % 2 != 0:
    print('Odd number of digits')



#########################################
# Question 3 - do not delete this comment
#########################################
grade = 90  # Replace ??? with an integer of your choice.
# Write the rest of the code for question 3 below here.
if grade < 0:
    print('Illegal grade')
elif grade <= 59:
    print('F')
elif grade <= 69:
    print('D')
elif grade <= 79:
    print('C')
elif grade <= 89:
    print('B')
elif grade <= 100:
    print('A')
else:
    print('Illegal grade')


#########################################
# Question 4 - do not delete this comment
#########################################
my_str = 'Betanir'  # Replace ??? with a string of your choice.
# Write the rest of the code for question 4 below here.

print(str.lower(my_str) == str.lower(my_str)[::-1])


