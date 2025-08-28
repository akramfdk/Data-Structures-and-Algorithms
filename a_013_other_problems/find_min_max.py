# a simple program that iterates through a list
# keeps track of the maximum and minimum values
# finally returns a tuple (max_value, min_value)

def find_min_max(my_list):
    min_val = my_list[0]
    max_val = my_list[0]

    for val in my_list:
        if val > max_val:
            max_val = val
        elif val < min_val:
            min_val = val

    return (max_val, min_val)

nums = [5, 3, 8, 1, 6, 9]
print(find_min_max(nums))