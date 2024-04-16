# In this part of the session, you will be solving the following problem:
# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 

# biggest_diff([10, 3, 5, 6]) → 7
# biggest_diff([7, 2, 10, 9]) → 8
# biggest_diff([2, 10, 7, 2]) → 8

def biggest_diff(nums):
    # make max_num variables equal to nums[0]
    # make a min_num variable equal to nums[0]
    # for num in nums:
    #   if num < min_num then set min_num to num
    #   if num > max_num set max_num to num
    # return max_num - min_num

    # variables for max number and minimum number
    max_num = nums[0]
    min_num = nums[0]
    # iterate through array
    for num in nums:
        # replace min_num if number is less than min_num
        if num < min_num:
            min_num = num
        # replace max_num if number is larger than max_num
        if num > max_num:
            max_num = num
    # return difference between min and max numbers
    return max_num - min_num

print(biggest_diff([10, 3, 5, 6]))
print(biggest_diff([7, 2, 10, 9])) 
print(biggest_diff([2, 10, 7, 2]))