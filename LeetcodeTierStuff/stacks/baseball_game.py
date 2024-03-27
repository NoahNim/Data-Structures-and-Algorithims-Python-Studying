# Understanding the problem:
# The problem wants me to return the sum of all scores on the record after applying each operation
# So operations is a list(array) of scores and operations to perform on them
# I will need to use a stack to solve this, as I am doing operations on a previous record (element) in the
# operations list


# Plan:
# create an empty stack using deque
# do a for loop to check each element (op) in operations
#   - if element in operations is equal to +, append the sum of the two previous scores to the stack
#   - else if element in operations is equal to C, pop it from the stack
#   - else if element in operations is equal to D, multiply the last two elements in the stack by two
#   - else if element is an integer, append it to the stack
# that for loop appends and removes items to the stack based on encountered elements in the operations list
# Pseudocode:
#   stack = deque([])
#   for op in operations
#   if op == + stack.append(stack[-1]+stack[-2])
#   if op == C stack.pop()
#   if op == D stack.append(2*stack[-1])
#   else stack.append(op)
#   return sum of stack

from collections import deque


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque([])
        for op in operations:
            if op == "+":
                stack.append(stack[-1]+stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2*stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)
