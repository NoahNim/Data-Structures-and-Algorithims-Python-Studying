# In a scenario where you're given a list of unique ID badges numbers 'nums' and a security checkpoint number 'target', your task is to find a pair of ID badges whose numbers sum up to the security checkpoint number.
# You should return the indices of these ID badges assuming no ID badge is scanned twice and there exists exactly one unique pair that meets the criteria.
# The order of indices in your result does not matter.
 
# Example 1:
# - Input: nums = [2, 7, 11, 15], target = 9
# - Output: [0, 1]
 
# Example 2:
# - Input: nums = [3, 2, 4], target = 6
# - Output: [1, 2]
 
# Example 3:
# - Input: nums = [3,3], target = 6
# - Output: [0,1]
 
# Constraints:
# - The length of the list 'nums' will be at least 2 and no more than 10^4
# - Each ID badge number will be an integer in the range from -10^9 to 10^9
# - The security checkpoint number 'target' will also be an integer within the same range
# - Assure only one valid pair exists that can be scanned to match the 'target' number

def find_id_pair(nums, target):


    # Write your plan below
    #######################
    # Create a variable nums_hash = {} that will store numbers in nums, key value pair is number and it's index
    # make an enumerate loop that is i, num in enumerate(nums)
    # make a variable called complement which is target - num
    # if complement in nums_hash then return [nums_hash[complement], i]
    # update nums_hash to have num and index in it
    #######################

    # hash to store numbers and associated index
    nums_hash = {}
    # loop through nums
    for i, num in enumerate(nums):
        # find targets complement
        complement = target - num
        # check if complement exists in num_hash
        if complement in nums_hash:
            return [nums_hash[complement], i]
        # update nums_hash
        nums_hash[num] = i    