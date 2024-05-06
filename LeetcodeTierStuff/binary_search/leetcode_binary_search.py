# plan
# make a variable left equal to 0
# make a variable right equal to length of nums minus 1
# do a loop while low is less than or equal to high
# # make a variable mid equal to left + (right - left) // 2
# # check if nums at mid is target, if so return mid
# # check if nums at mid is greater than high, if so then set right to mid + 1
# # if it's less than target set left to mid - 1
# return -1 if loop ends without finding target

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            # left + (right - left) divided by 2 calculates the middle
            mid = left + (right - left) // 2
            # check if nums at mid is the target
            if nums[mid] == target:
                return mid
            # if it's not see if it's greater or less than the target, shifting right and left depending on that since nums is in ascending order
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return - 1