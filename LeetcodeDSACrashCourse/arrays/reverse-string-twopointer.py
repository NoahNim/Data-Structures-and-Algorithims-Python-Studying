# make a left point = 0 and a right pointer = length of array minus 1
# make a while loop of left < right
# # switch s[left] and s[right], using s[left]. s[right] = s[right], s[left]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        