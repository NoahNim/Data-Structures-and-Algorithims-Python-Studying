# Imagine you are analyzing the performance of students in a particular test, and you have their scores stored in an integer array named 'nums', where each element represents the unique score of a student.
# Your task is to select a subset of these scores, precisely 'k' of them, in such a way that the variation between the highest score and the lowest score within this subset is minimized.
# This variation is the numeric difference between the highest and the lowest scores.
# You need to find and return this minimum possible variation.
 
# Example 1:
# Input: nums = [90], k = 1
# Output: 0
# Explanation: Selecting the score of the only student gives a subset [90].
# The difference between the highest and lowest score in this subset is 0, which is the minimum possible variation.
 
# Example 2:
# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: By selecting scores of any two students, the minimum variation in scores can be achieved by either selecting the scores [7, 9] or [1, 3], resulting in a variation of 2 in both cases.
# Hence, the minimum possible variation is 2.
 
# Constraints:
# - The number of students (and thus the size of the 'nums' array) ranges between 1 and 1000.
# - Each student's score is a non-negative integer not exceeding 10^5.
# - The value of 'k' will at least be 1 and not more than the number of students.

def optimalScoreRangeFinder(nums, k):
    if len(nums) < 1:
        return 0

    nums = sorted(nums)
    result = float('inf')
    left = 0

    for right in range(k - 1, len(nums)):
        result = min(result, nums[right] - nums[left])
        left += 1
    return result