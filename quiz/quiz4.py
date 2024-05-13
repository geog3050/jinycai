######################################################################
# Edit the following function definition, replacing the words
# 'name' with your name and 'hawkid' with your hawkid.
#
# Note: Your hawkid is the login name you use to access ICON, and NOT
# your firstname-lastname@uiowa.edu email address.
#
# def hawkid():
#     return(["Caglar Koylu", "ckoylu"])
######################################################################
def hawkid():
    return(["Jinyi Cai", "jinycai"])

######################################################################
# DON'T MAKE ANY CHANGES HERE.
if (not hawkid()[0] or not hawkid()[1]) or (hawkid()[1] == "hawkid"):
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
    print('### Otherwise, the Autograder will assign 0 points.')
    exit(-1)
else:
    info = hawkid()
    print(info[0])
    print(info[1])
######################################################################

######################################################################
# Problem 1 - Getting Input - (40 Points)
#
# Specification: You are expected to ask for three main inputs:
#     1. mode: This input will be a string given by the user to determine
#              the calculation method. Valid inputs are 'min', 'max', 'avg'.
#     2. count: This input will be an integer given by the user to indicate
#               how many more inputs/values are expected to be given. These
#               new values will be added to a list to be used later in the
#               calculations.
#     3. values: These inputs will be floats. You are expected to read user
#                input 'count' times to get all the values. All of the values
#                should be stored in a list to be used later.
#
# What is expected?
#     After you get all the inputs from the user, print the following information
#     in order:
#           - Print 'mode' variable value (1 Point)
#           - Print 'count' variable value (1 Point)
#           - Print length of the list you have just created (1 Point)
#           - Print the list you have just created (5 Points)
#     All of the prints should be in separate print statements. Please, don't
#     forget that the order is very important.
#
# Note: Don't forget that input() function returns a string, not a number
#       even though you give a number as an input. Therefore, be careful
#       about data type conversions.
#
# Example Input/Output:
#     Assume that you are given the following inputs:
#       avg
#       4
#       123
#       14234
#       25435
#       14
#
#     Your solution for Problem 1 should print the following:
#       Caglar Koylu (Your name will be here)
#       ckoylu (Your hawkid will be here)
#       avg
#       4
#       4
#       [123.0, 14234.0, 25435.0, 14.0]
######################################################################


# WRITE YOUR SOLUTION FOR PROBLEM 1 HERE.
    
# handle exception to check if the input is one of the min, max or avg
def handle_mode_input(text):
    while True:
        mode = input(text)
        try:
            if mode not in ['min', 'max', 'avg']:
                raise ValueError("Input mode is not min, max or avg!")
            break
        except ValueError as e:
            print(e)
    return mode

# handle exception to check if the input is an integer
def handle_int_input(text):
    while True:
        input_item = input(text)
        try:
            item_int = int(input_item)
            break
        except ValueError:
            print ("Input is not an integer!")
    return item_int

# handle exception to check if the input is a float number
def handle_float_input(text):
    while True:
        input_item = input(text)
        try:
            item_int = float(input_item)
            break
        except ValueError:
            print ("Input is not an float number!")
    return item_int

# set the order index based on number value
def set_order_by_number(number):
    order = number + "th" 
    if len(number) == 1 or (len(number) > 1 and number[-2] != '1'):
        if number[-1] == '1':
            order = number + "st"
        elif number[-1] == '2':
            order = number + "nd"
        elif number[-1] == '3':
            order = number + "rd"
    return order

# get the input information
def get_input():
    mode = handle_mode_input("Please enter a mode (min, max or avg): ") 
    count_int = handle_int_input("Please enter an integer count: ")
    value_list = []
    for i in range(count_int):
        order = set_order_by_number(str(i+1))
        value_item = handle_float_input(f"Please enter the {order} float number: ")
        value_list.append(value_item)
    return [mode, count_int, len(value_list), value_list]

# print user information and input information
def print_info_and_input1():
    input_list = get_input()
    info_list = hawkid()
    output_list = info_list + input_list 
    for item in output_list:
        print(item)

# print_info_and_input1()

######################################################################
# Problem 2 - Find the Minimum/Maximum/Average - (60 Points)
#
# Specification: In this part of the homework, you are expected to compute
# a value for the given 'mode'. Therefore, your code has to have three main
# code blocks:
#     1. Finding Minimum: If the value of 'mode' is 'min', find the minimum
#                         element in the list. Then, print its value.
#     2. Finding Maximum: If the value of 'mode' is 'max', find the maximum
#                         element in the list. Then, print its value.
#     3. Finding Average: If the value of 'mode' is 'avg', compute the average
#                         of all elements in the list. Computation is basically:
#                               (Sum of all elements)/(Number of elements)
#
# Note: BE CAREFUL. YOU CANNOT USE ANY LIBRARIES OR PYTHON'S BUILT-IN
#       min, max, sum operations. You are expected to implement these operations
#       by your own. Such an use of those functions are not allowed and may cause
#       you loose points.
#
# Hint: These three code blocks depend on the value of 'mode'. Therefore,
#       using a conditional branches may help you to perform different
#       operations in different code blocks. Also, in order to traverse
#       over each element in the list one by one iteration concepts can
#       be very helpful.
#
# Example Input/Output:
#     Assume that you are given the following inputs:
#       avg
#       4
#       123
#       14234
#       25435
#       14
#
#     Your solution for Problem 1 & 2 should print the following:
#       Caglar Koylu (Your name will be here)
#       ckoylu (Your hawkid will be here)
#       avg
#       4
#       4
#       [123.0, 14234.0, 25435.0, 14.0]
#       9951.5
######################################################################


# WRITE YOUR SOLUTION FOR PROBLEM 2 HERE.
# get the minimum value
def get_min(value_list):
    min = value_list[0]
    for value in value_list[1:]:
        if min > value:
            min = value
    return min

# get the maximum value
def get_max(value_list):
    max = value_list[0]
    for value in value_list[1:]:
        if max < value:
            max = value
    return max

# get the average value
def get_avg(value_list):
    sum = 0
    for value in value_list:
        sum += value
    avg = sum/len(value_list)
    return avg

# print user information and input information with the calculated reuslt
def print_info_and_input2():
    input_list = get_input()
    info_list = hawkid()
    mode = input_list[0]
    value_list = input_list[-1]

    if mode == 'avg':
        cal_result = get_avg(value_list)
    elif mode == 'min':
        cal_result = get_min(value_list)
    else:
        cal_result = get_max(value_list)

    output_list = info_list + input_list + [cal_result]
    
    for item in output_list:
        print(item)

print_info_and_input2()
######################################################################

