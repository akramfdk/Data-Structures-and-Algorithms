# merging two sorted lists
def merge(lst1, lst2):
    combined = []
    i = 0
    j = 0

    while i<len(lst1) and j<len(lst2):
        if lst1[i] <= lst2[j]:
            combined.append(lst1[i])
            i += 1
        else:
            combined.append(lst2[j])
            j += 1

    while i < len(lst1):
        combined.append(lst1[i])
        i += 1
    
    while j < len(lst2):
        combined.append(lst2[j])
        j += 1

    return combined

# dividing a list into two halves recursively until there is one element
# then combining on the way back using merge function
def merge_sort(my_list):

    if len(my_list) <= 1:
        return my_list
    
    mid_val = len(my_list)//2
    left = my_list[:mid_val]
    right = my_list[mid_val:]

    return merge(merge_sort(left), merge_sort(right))

num_list = [3, 5, 2, 6, 4, 1]
print(merge_sort(num_list))
