''' Exercise #10. Computational Thinking and Programming.'''
###############################################################
# do not delete or change this import
###############################################################
import numpy as np

###############################################################
# do not delete or change load_luna_park_data_to_lists function
###############################################################
def load_luna_park_data_to_lists(csv_file):
    with open(csv_file) as f: # "with" statement handles file opening and closing
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
    pass  # delete this pass command and write your code instead


#########################################
# Question 2 - do not delete this comment
#########################################
def max_use(data):
    pass  # delete this pass command and write your code instead


#########################################
# Question 3 - do not delete this comment
#########################################
def average_use_per_kid(data):
    pass  # delete this pass command and write your code instead


#########################################
# Question 4 - do not delete this comment
#########################################
def usage_variance_per_ride(data):
    pass  # delete this pass command and write your code instead


#########################################
# Question 5 - do not delete this comment
#########################################
def no_use(data):
    pass  # delete this pass command and write your code instead


#########################################
# Question 6 - do not delete this comment
#########################################
def more_than_25(data):
    pass  # delete this pass command and write your code instead


#########################################
# Question 7 - do not delete this comment
#########################################
def heavy_user(data, names):
    pass  # delete this pass command and write your code instead


#########################################
# Question 8 - do not delete this comment
#########################################
def least_popular_ride(data, rides):
    pass  # delete this pass command and write your code instead


#########################################
# Question 9 - do not delete this comment
#########################################
def fix_last_kid(data):
    pass  # delete this pass command and write your code instead


#########################################
# Question 10 - do not delete this comment
#########################################
def fix_wrong_minus(data):
    pass  # delete this pass command and write your code instead


#########################################
# Question 11 - do not delete this comment
#########################################
def bad_luck_rides(data,rides):
    pass  # delete this pass command and write your code instead


#########################################
# Question 12 - do not delete this comment
#########################################
def sort_users_descending(data, names):
    pass  # delete this pass command and write your code instead

