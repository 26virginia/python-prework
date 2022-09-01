#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    max = a_list[0]
    for i in range(len(a_list)):
        if a_list[i] > max:
            max = a_list[i]
    return max
a_list = [1, 2, 3, 4, 5]
print(max_num_in_list(a_list))