''' Exercise #4. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
n = 5  # Replace ??? with an integer of your choice.
# Write the rest of the code for question 1 below here.
flag = 0
for i in range(2,n):
    if n % i == 0:
        flag = 1
        break

if flag == 1:
    print(n,'is NOT a prime number')
else:
    print(n,'is a prime number')



#########################################
# Question 2 - do not delete this comment
#########################################
m = 10 # Replace ??? with an integer of your choice.
n = 3 # Replace ??? with an integer of your choice.
# Write the rest of the code for question 2 below here.
sum = 0
num = 0
for i in range(min(n,m)+1,max(n,m)):
    if i % 2 != 0:
        sum += i
        num += 1
try:
    print(sum/num)
except ZeroDivisionError:
    print(0.0)



#########################################
# Question 3 - do not delete this comment
#########################################
p = 5 # Replace ??? with an integer of your choice.
# Write the rest of the code for question 3 below here.
for i in range(p,0,-1):
    for j in range(i):
        print(i,end='')
    print()



#########################################
# Question 4 - do not delete this comment
#########################################
lst4 = [0, 5.4, 0, 7, 6, 8.1, 3, 6, 0, 3] # Replace ??? with a list of your choice.
# Write the rest of the code for question 4 below here.
lst6 = list(set(lst4))  # There wasn't an exception for this lol!
print('New list is',lst6)


#########################################
# Question 5 - do not delete this comment
#########################################
lst5 = ['hi', 'ho', 'ho', 'ho', 'no', 1, 1, 'do', 'you', 'copy'] # Replace ??? with a list of your choice.
# Write the rest of the code for question 5 below here.


flag = 0
for i in range(len(lst5)-1):
    if lst5[i] == lst5[i+1]:
        print(lst5[i])
        flag = 1

if flag == 0:
    print('No repetitions were found!')