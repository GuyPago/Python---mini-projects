''' Exercise #3. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
lst = [1, 5.4, 7] # Replace ??? with a list of your choice.
# Write the rest of the code for question 1 below here.
lst2 = []
for i in lst:
    lst2.append(lst.index(i))
print(lst2)

#########################################
# Question 2 - do not delete this comment
#########################################
lst = [2,3,23,2,31,2,3,4,21,4,24,21,3,214,1,24,2,4] # Replace ??? with a list of your choice.
# Write the rest of the code for question 2 below here.


lst_3 = []
for i in range(len(lst)-1,-1,-2):
    lst_3.append(lst[i])
print(lst_3)


#########################################
# Question 3 - do not delete this comment
#########################################
lst = [2, 1, 1, 4,6,6,6,19] # Replace ??? with a list of integer numbers of your choice.
# Write the rest of the code for question 3 below here.
sum = 0
for i in lst:
    if i % 2 == 0:
        sum += i
print(f'List’s even numbers sum is: {sum}')


#########################################
# Question 4 - do not delete this comment
#########################################
x = 2 # Replace ??? with a value of your choice.
lst = ['hi','ok',2,3] # Replace ??? with a list of your choice.
# Write the rest of the code for question 4 below here.
print(x in lst)


#########################################
# Question 5 - do not delete this comment
#########################################
lst = [0, 5.4, 7, 6,5,2,3,4,2] # Replace ??? with a list of your choice.
# Write the rest of the code for question 5 below here.

while len(lst) < 7:
    lst.append(0)

while len(lst) > 7:
    lst.pop()
print('New list is',lst,sep='\n')