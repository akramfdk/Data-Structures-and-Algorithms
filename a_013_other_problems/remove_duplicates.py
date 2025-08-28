# given a list of non decreasing integers, remove duplicates from the list
# Using a two pointer method
# The duplicates are removed in a single sweep
# Time Complexity O(n)
# The function returns the size of the list with unique elements

def remove_duplicates(my_list):
    if not my_list:
        return 0
    
    write_pointer = 1

    for read_pointer in range(1, len(my_list)):
        if my_list[read_pointer] != my_list[read_pointer - 1]:
            my_list[write_pointer] = my_list[read_pointer]
            write_pointer += 1

    return write_pointer


my_list = [0, 0, 1, 1, 1, 2, 3, 3, 4, 4, 4]
print(remove_duplicates(my_list))
print(my_list)

my_list_2 = []
print(remove_duplicates(my_list_2))
print(my_list_2)

my_list_3 = [3]
print(remove_duplicates(my_list_3))
print(my_list_3)