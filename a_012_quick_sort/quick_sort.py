# taking the left element as the pivot
# putting the pivot in its right position and returning this position
def pivot(my_list, left, right):
    pivot_index = left
    swap_index = left

    for i in range(left+1, right+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            my_list[swap_index], my_list[i] = my_list[i], my_list[swap_index]
    
    my_list[pivot_index], my_list[swap_index] = my_list[swap_index], my_list[pivot_index]

    return swap_index

# recursively calls itself till all values are put in the right position
def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

my_list = [3, 5, 2, 6, 1, 4]
print(quick_sort(my_list))
