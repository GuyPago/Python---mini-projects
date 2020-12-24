''' Exercise #8. Computational Thinking and Programming.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def write_text_to_file(txt, file_path):
    with open(file_path, 'w') as f:
        f.write(txt)


#########################################
# Question 2 - do not delete this comment
#########################################
def get_file_length(file_path):
    with open(file_path, 'r') as f:
        return len(f.read())


#########################################
# Question 3 - do not delete this comment
#########################################
def sum_file_nums(file_path):
    summa = 0
    with open(file_path, 'r') as f:
        for num in f.readlines():
            summa += float(num)
    return summa


#########################################
# Question 4 - do not delete this comment
#########################################
def parse_file_to_list(file_path, delimiter):
    with open(file_path, 'r') as f:
        return f.read().split(delimiter)


def parse_file_to_matrix(file_path, delimiter):
    mat = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            mat += [line.strip().split(delimiter)]
    return mat

#############################################
# BONUS Question - do not delete this comment
#############################################
def count_courses_intersection(course2students):
    pass  # if you wish, delete this pass command and write your code instead


# Auxiliary function for counting the intersection just to keep things simple.
def intersection_of_course1_and_course2(course2students, course1, course2):
    pass  # if you wish, delete this pass command and write your code instead
