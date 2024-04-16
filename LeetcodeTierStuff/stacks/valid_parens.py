# Task: Check whether all criteria is met
## Open brackets must be closed by same type
## Open brackets must be closed in the correct order
## Every closing bracket has a corresponding bracket of the same tyep
# Does string only contain ()[]{}?

# Plan
#   stack = deque([])
# pairs = {} a hash map of open and closing parentheses
# Add to stack while char is an open parenthesis
#  iterate through list for char in s:
    # check if char in pairs
    #   if char in pairs:
    #       stack.push(char)
    #  check if stack length is 0 or char is not paired to the bracket popped from stack return False if those cases are hit
    #   if len(stack) == 0 or char != pairs[stack.pop()]
    #       return False
# check if stack length is 0, if it is that means the loop succesfully iterated finding the correct matching pairs so return True
# otherwise False can be return

from collections import deque

def bracket_sequence_validator(s):
    stack = deque([])
    pairs = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    for char in s:
        if char in pairs:
            stack.append(char)
        elif len(stack) == 0 or char != pairs[stack.pop()]:
            return False
    if len(stack) == 0:
        return True
    else:
        return False