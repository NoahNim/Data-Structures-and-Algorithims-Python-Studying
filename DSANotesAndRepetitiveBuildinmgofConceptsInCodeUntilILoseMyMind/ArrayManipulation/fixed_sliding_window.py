# Fixed Sliding Window
# Typically has left and right pointers to represent the boundaries of the window
# We can keep track of the contents using a hash table or a set
# In contrast to a two pointer, which is focused on analyzing the two points, the sliding glass focuses on analyzing what is between those points
# The aim of sliding window is to reduce the use of nested loops and instead replace it with a single loop, reducing time complexity from O(n^2) to O(n)
# This structure is useful when we want to find subarrays or substrings that meet a given condition within a given length.
# demo: contains duplicates https://leetcode.com/problems/contains-duplicate-ii/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# asking is there a subarray with the size of k that contains uplicates
# use a left and right pointer to make the sliding window like so:
# [1,2,3,1]
#  LR
# [1,2,3,1]
#  L R
# [1,2,3,1]
#  L   R
# [1,2,3,1]
#  L     R
# The window grows on each iteration
# The only time we move the left pointer is if we exceed our k limit
# so create a set called window = {}
# each time we analyze R pointer, we check if it is in window. if it is not add it to the window, if it is we can return True
# We also keep track if the indices count between L and R is less than or equal to k by finding the distance between L and R by substracting the indices of of L and R to see if the result is less than or equal to the k constraint
# if the difference (window constraint) is bigger than k, the left pointer moves over by one
# [1,2,3,4,6,1]
#    L     R
# at this point the window set would be window = {1, 2, 3}
# but because 1 is no longer in the window, it must be removed and then 6 can be added
# window = {2, 3, 6}
# after moving L pointer window = {3, 4, 6} as 2 is then removed from set
# [1,2,3,4,6,1]
#      L     R
# after this the loop would end as the R pointer leaves the array, if the loop exits False can just be returned

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0
        for right in range(len(nums)):
            if right-left > k:
                window.discard(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False
