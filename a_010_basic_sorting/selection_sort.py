my_list = [3, 2, 5, 1, 6, 4]

# we run the outer loop from i = 0 to len(list) - 1
# during each iteration we bring the smallest element from j = i+1 to end
# swap it with the ith element
def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j

        if min_index != i:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
        
    return my_list


print(selection_sort(my_list))
