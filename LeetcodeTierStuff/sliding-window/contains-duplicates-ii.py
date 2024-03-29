# the problem is asking if with the window/range of k subarray there are duplicate numbers

# create a set called window
# window = set()
# create a left pointer
# left = 0
# then loop through the with right in range of length of nums
# for right in range(len(nums))
# check if right - left > k, if it is remove nums[left] from window and increase left by 1
# window.discard(nums[left])
# left += 1
# check if nums[right] is in window, if it is return True
# if it's not add it to the window with window.add(nums[right])
# if the loop exits return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0
        for right in range(0, len(nums)):
            if right - left > k:
                window.discard(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False
