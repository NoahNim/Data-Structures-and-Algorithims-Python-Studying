# Imagine yourself as an ingenious burglar who has eyed a unique street for your next heist.
# This street is not ordinary as it forms a closed loop, with each home filled with a varying amount of loot.
# However, these homes have an advanced security system that triggers an alarm if any two adjacent homes are burglarized on the same evening.
# Given an array of integers, nums, where each element signifies the treasure in each house, devise a strategy to maximize your haul without risking capture.
# Your task is to figure out the largest sum of money you can accumulate without setting off the alarms.
 
# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: Optimal approach is to rob house 2, avoiding houses 1 and 3 due to their adjacency and the risk of triggering alarms.
 
# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Maximizing loot by robbing houses 1 and 3 for a total of 4.
# Robbing any adjacent houses is not viable due to the security system.
 
# Example 3:
# Input: nums = [1,2,3]
# Output: 3
 
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000