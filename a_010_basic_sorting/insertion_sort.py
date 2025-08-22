my_list = [3, 2, 5, 1, 6, 4]

# We go from i=1 to len(list)
# during each iteration we place ith element in the correct position
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        i_val = my_list[i]
        j = i-1

        while j>=0 and my_list[j] > i_val:
            my_list[j+1] = my_list[j]
            j -= 1

        my_list[j+1] = i_val

    return my_list

print(insertion_sort(my_list))