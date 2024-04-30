# Imagine you are given a list called 'nums' containing distinct integers sorted in non-decreasing order, and another integer named 'target'.
# Your task is to find the position of 'target' within 'nums'.
# Should 'target' be present in 'nums', return its array index.
# If 'target' is absent from 'nums', return -1.
# Design your solution to operate with a time complexity of O(log n), leveraging the efficiency of binary search.
 
# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: Since 9 is present in 'nums', its index 4 is returned.
 
# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: Given 2 does not appear in 'nums', -1 is returned.
 
# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All integers in 'nums' are distinct.
# 'nums' is sorted in non-decreasing order.

def locate_element(nums, target):
    # make low and high variables, low set to 0 and high set to length of list -1
    # while low <= high, we calculcate the middle by adding low and high // 2
    #   check if middle is target, if it is return middle index
    #   else if mid > target, then I'd set high to be mid - 1
    #   else set low to mid + 1
    # return -1 if the loop ends
    # create low and high
    low, high = 0, len(nums) - 1
    # loop through list using indexes at low and high
    while low <= high:
        # find middle index
        mid = low + high // 2
        # check if middle is target
        if nums[mid] == target:
            return mid
        # if the mid is greater target set high to be one less thean mid
        elif nums[mid] > target:
            high = mid - 1
        # if the mid is less than the target, set low to be one more than mid
        else:
            low = mid + 1
    # return -1 if loop ends
    return -1
