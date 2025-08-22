my_list = [3, 2, 5, 1, 6, 4]

# in bubble sort we perform n-1 outer loop iterations
# during each iteration, we bubble the largest element towards the end
# can be made adaptive by checking if swaps occured during any iteration
# if not, means the list is sorted and break out
def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        has_swapped = False
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                has_swapped = True
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

        if not has_swapped:
            break

    return my_list

print(bubble_sort(my_list))