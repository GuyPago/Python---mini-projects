''' Exercise #10. Computational Thinking and Programming.'''
###############################################################
# do not delete or change this import
###############################################################
import numpy as np


###############################################################
# do not delete or change load_luna_park_data_to_lists function
###############################################################
def load_luna_park_data_to_lists(csv_file):
    with open(csv_file) as f:  # "with" statement handles file opening and closing
        rides_list = f.readline().rstrip().split(',')[1:]
        data_table, names_list = [], []
        for line in f:
            line_tokens = line.rstrip().split(',')
            name = line_tokens[0]
            names_list.append(name)
            data_table.append([int(count) for count in line_tokens[1:]])  # add next table row
    return rides_list, names_list, data_table


#########################################
# Question 1 - do not delete this comment
#########################################
def load_luna_park_data_to_arrays(csv_file):
    rides_list, names_list, data_table = load_luna_park_data_to_lists(csv_file)
    rides_list = np.array(rides_list)
    names_list = np.array(names_list)
    data_table = np.array(data_table)

    return rides_list, names_list, data_table


#########################################
# Question 2 - do not delete this comment
#########################################
def max_use(data):
    return np.max(data)


#########################################
# Question 3 - do not delete this comment
#########################################
def average_use_per_kid(data):
    return np.average(data, axis=1)


#########################################
# Question 4 - do not delete this comment
#########################################
def usage_variance_per_ride(data):
    return np.var(data, axis=0)


#########################################
# Question 5 - do not delete this comment
#########################################
def no_use(data):
    return np.any(np.sum(data, axis=0) == 0)


#########################################
# Question 6 - do not delete this comment
#########################################
def more_than_25(data):
    return np.sum(np.sum(data, axis=0) > 25)


#########################################
# Question 7 - do not delete this comment
#########################################
def heavy_user(data, names):
    m = np.sum(data, axis=1)
    return names[m.argmax()]


#########################################
# Question 8 - do not delete this comment
#########################################
def least_popular_ride(data, rides):
    m = np.sum(data, axis=0)
    return rides[m.argmin()]


#########################################
# Question 9 - do not delete this comment
#########################################
def fix_last_kid(data):
    new_data = np.copy(data)
    new_data[-1] += 5
    return new_data


#########################################
# Question 10 - do not delete this comment
#########################################
def fix_wrong_minus(data):
    new_data = np.copy(data)
    new_data[new_data == -1] = 1
    return new_data


#########################################
# Question 11 - do not delete this comment
#########################################
def bad_luck_rides(data, rides):
    return rides[np.sum(data, axis=0) % 11 == 0]


#########################################
# Question 12 - do not delete this comment
#########################################
def sort_users_descending(data, names):
    sm = np.sum(data, axis=1)

    return names[np.argsort(sm)][::-1]
