''' Exercise #5. Computational Thinking and Programming.'''
import math as m


#########################################
# Question 1 - do not delete this comment
#########################################
def is_char_in_str(s1, c1):
    return c1 in s1


#########################################
# Question 2 - do not delete this comment
#########################################
def is_in_range(lst2, a, b):
    if len(lst2) > 0:
        return (max(lst2) < b) and (min(lst2) > a)
    else:
        return True


#########################################
# Question 3 - do not delete this comment
#########################################
def upper_list_strings(lst3):
    new_lst = []
    for i in lst3:
        new_lst.append(i.upper())
    return new_lst


#########################################
# Question 4 - do not delete this comment
#########################################
def log10_list(lst4):
    new_lst = []
    for i in lst4:
        new_lst.append(m.log10(i))
    return new_lst


#########################################
# Question 5 - do not delete this comment
#########################################
def is_palindrom(s5):
    return s5 == s5[::-1]
