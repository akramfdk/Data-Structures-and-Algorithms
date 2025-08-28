# this problem removes all occurences of value in the list "nums"
# two pointer method
# one pointer or counter goes through the list
# other tracks the modified list with occurences of "value" removed from it
def remove_element(nums, value):

    i = 0

    for j in range(len(nums)):
        if nums[j] != value:
            nums[i] = nums[j]
            i += 1

    value_count = len(nums) - i
    for _ in range(value_count):
        nums.pop()

    return nums

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(remove_element(nums, 1))