# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# make a stack and put root in the stack
# while stack is not empty
# take the current value called visited out of the stack (use pop)
# add it to a total_sum variable
# use a depth first traverdal, so if visited.right exists append it and if visited.left exists append it
# return the total sum

from collections import deque


def tree_sum(root):
    if root is None:
        return 0
    total_sum = 0
    stack = deque()
    stack.append(root)
    while stack:
        visited = stack.pop()
        total_sum += visited.val
        if visited.right:
            stack.append(visited.right)
        else:
            pass
        if visited.left:
            stack.append(visited.left)
        else:
            pass
