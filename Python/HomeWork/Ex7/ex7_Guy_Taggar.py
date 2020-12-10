''' Exercise #7. Computational Thinking and Programming.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def range_dict(a, b):
    dic = {}
    for i in range(a, b + 1):
        dic[i] = dic.get(i, [i])
    return dic


#########################################
# Question 2 - do not delete this comment
#########################################
def merge_dictionaries(d1, d2):
    dic = d1.copy()
    dic.update(d2)
    return dic


#########################################
# Question 3 - do not delete this comment
#########################################
def most_popular_digit(num):
    dic = {}
    for i in str(num):
        dic[i] = dic.get(i, 0) + 1
    return max(dic, key=dic.get)


#########################################
# Question 4 - do not delete this comment
#########################################
def most_common_value_in_dict(d):
    dic = {}
    for i in d.values():
        dic[i] = dic.get(i, 0) + 1
    return max(dic, key=dic.get)


#############################################
# BONUS Question - do not delete this comment
#############################################
def swap_students_courses(student2courses):
    dic = {}
    for student in student2courses:
        for course in student2courses[student]:
            dic[course] = dic.get(course, [])
            dic[course].append(student)
    return dic
