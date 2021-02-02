''' Exercise #9. Computational Thinking and Programming.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def top_of_genre(in_file_name, out_file_name, genre):
    with open(in_file_name, 'r') as f:
        first_line = f.readline()
        count = 0
        final_line = ''
        for line in f:
            revenue = line.strip().split(',')[10]
            if genre.lower() in line.strip().split(',')[2].split(';'):
                if float(revenue) > count:
                    count = float(revenue)
                    final_line = line
        with open(out_file_name, 'w') as f1:
            f1.write(first_line + final_line)
    return None

top_of_genre('IMDB.csv','Gezza.csv','comedy')
#########################################
# Question 2 - do not delete this comment
#########################################
def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


#########################################
# Question 3 - do not delete this comment
#########################################
def get_key_by_value(d, val):
    if val in d.values():  # Improves efficiency
        for key in d:
            if d[key] == val:
                return key
    return None


#########################################
# Question 4 - do not delete this comment
#########################################
def get_top3_students(students_and_grades):
    top = sorted(students_and_grades, key=lambda x: x[1], reverse=True)
    return [top[i][0] for i in range(min(3, len(top)))]  # if lst contains less than 3 students


#############################################
# BONUS Question - do not delete this comment
#############################################
def merge_2_sorted_lists(left, right):
    merged = []
    left_i = 0
    right_i = 0
    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            merged.append(left[left_i])
            left_i += 1
        else:
            merged.append(right[right_i])
            right_i += 1
    merged += left[left_i:] + right[right_i:]
    return merged


def merge_3_sorted_lists(l1, l2, l3):
    return merge_2_sorted_lists(merge_2_sorted_lists(l1, l2), l3)
