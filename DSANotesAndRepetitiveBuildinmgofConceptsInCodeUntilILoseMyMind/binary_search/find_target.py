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

    # Initialize two pointers: 'low' at the start of the array and 'high' at the end of the array.
    # These pointers define the current search range within the array.
    low, high = 0, len(nums) - 1

    # The while loop continues as long as 'low' is less than or equal to 'high'.
    # This condition ensures that the search range is valid.
    while low <= high:
        # Calculate the middle index of the current search range.
        # This is done by adding 'low' and 'high' and then dividing by 2.
        # Using '//' for division to get an integer result.
        mid = (low + high) // 2

        # Check if the element at the middle index ('mid') is the target.
        # If yes, return the index 'mid' as the target is found.
        if nums[mid] == target:
            return mid
        # If the element at 'mid' is greater than the target,
        # it means the target, if present, must be in the left half of the current range.
        # So, update 'high' to 'mid - 1' to search in the left half in the next iteration.
        elif nums[mid] > target:
            high = mid - 1
        # If the element at 'mid' is less than the target,
        # it means the target, if present, must be in the right half of the current range.
        # So, update 'low' to 'mid + 1' to search in the right half in the next iteration.
        else:
            low = mid + 1

    # If the loop exits without returning, it means the target is not present in the array.
    # In this case, return -1 as specified in the problem.
    return -1