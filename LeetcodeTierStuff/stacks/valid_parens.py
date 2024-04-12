# Task: Check whether all criteria is met
## Open brackets must be closed by same type
## Open brackets must be closed in the correct order
## Every closing bracket has a corresponding bracket of the same tyep
# Does string only contain ()[]{}?

# Plan
#   stack = deque()
#   open = hash of "({["
#   closed = hash of ")}]"
#   i = 0
# Add to stack while char is an open parenthesis
# for char in s:
#   if char in open:
#       stack.push(char)
#   else:
#       closer = closed.index(char)
#       