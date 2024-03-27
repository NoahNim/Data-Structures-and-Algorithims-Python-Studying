# Understand
# I want to find the nexting depth of parentheses in a string
# the first parentheses "(" in a string is a depth of 0, the second parentheses is a depth of 1
# so I basically want to count the amount of parentheses "(" before I hit ")"

# Plan:
# Using deque create an empty stack
# make a variable call curr_depth equal to 0
# make a variable called highest_depth equal to 0
# make a variable called stack count equal to zero
# do a for loop of the string where char (character) is the element being analyzed
# check if the current character is "(", if it is append it to the stack, increase curr_depth by 1
# also increase stack_count by 1
# check if the current character is ")", if it is pop from stack and decrease stack_count and
#   check if cur_depth is greater than highest_depth, if it is set highest_depth to curr_depth
#   set curr_depth to 0
#   if stack_count is greater than curr_depth, set curr_depth to stack_count
# return highest depth

# Pseodocode:
# stack = []
# highest_depth = 0
# curr_depth = 0
# for char in s:
#   if char == "(":
#       stack.append(char)
#       curr_depth + 1
#   elif char == ")":
#       stack.pop()
#       if curr_depth > highest_depth:
#           highest_depth = curr_depth
#       curr_depth = 0
#       if stack_count > curr_depth:
#           curr_depth = stack_count
# return highest_depth
from collections import deque


class Solution:
    def maxDepth(self, s: str) -> int:
        if len(s) == 0:
            return 0
        stack = deque([])
        highest_depth = 0
        curr_depth = 0
        stack_count = 0
        for char in s:
            if char == "(":
                stack.append(char)
                stack_count += 1
                curr_depth += 1
            elif char == ")":
                stack.pop()
                stack_count -= 1
                if curr_depth > highest_depth:
                    highest_depth = curr_depth
                curr_depth = 0
                if stack_count > curr_depth:
                    curr_depth = stack_count
        return highest_depth
