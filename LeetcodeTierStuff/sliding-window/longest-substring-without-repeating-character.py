# Understand
# I want to find the length of a "substring" before it hits a repeating character, so when it hits a repeating
# character I want to stop counting that substring

# Plan
# create an empty set called window
# create a left pointer equal to 0
# create a right pointer equal to 0
# create a variable longest_streak set to 0
# create a variable current_streak set to 0
# do a while loop of while left is less than streak of s
# in the while loop check if s[right] is in in the set
#       if it is then discard s[left] and increase left by 1
#       check if current_streak is greater than longest_streak, if it is replace longest with current
#       set current_streak to 0
#   put s[right] in the set
#   increase current_streak by 1
#   increase right by 1
# return longest_streak

# Pseudocode
# function
#   window = set()
#   left = 0
#   right = 0
#   longest_streak = 0
#   current_streak = 0
#   while right < len(s)
#       while s[right] in window
#           window.discard(s[left])
#           left += 1
#           if current_streak > longest_streak
#               longest_streak = current_streak
#           curent_streak = 0
#       window.add(s[right])
#       current_streak += 1
#       right += 1
#   return longest_streak

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        right = 0
        longest_streak = 0
        current_streak = 0
        while right < len(s):
            while s[right] in window:
                window.discard(s[left])
                left += 1
                if current_streak > longest_streak:
                    longest_streak = current_streak
                current_streak = len(window)
            window.add(s[right])
            current_streak += 1
            right += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
        return longest_streak
