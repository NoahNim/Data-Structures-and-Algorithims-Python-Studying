# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# make a stack and put root in the stack
# while stack is not empty
# take the current value called visited out of the stack (use pop)
# if visited is the target, return True
# use a depth first traverdal, so if visited.right exists append it and if visited.left exists append it
# if the loop exits without finding the target, return False

from collections import deque


def tree_includes(root, target):
    if root is None:
        return False
    stack = deque()
    stack.append(root)
    while stack:
        visited = stack.pop()
        if visited.val == target:
            return True
        if visited.right:
            stack.append(visited.right)
        else:
            pass
        if visited.left:
            stack.append(visited.left)
        else:
            pass
    return False
