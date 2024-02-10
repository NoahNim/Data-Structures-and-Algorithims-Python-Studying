# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque


def tree_value_count(root, target):
    if root is None:
        return 0
    count = 0
    stack = deque()
    stack.append(root)
    while stack:
        visited = stack.pop()
        if visited.val == target:
            count += 1
        if visited.right:
            stack.append(visited.right)
        else:
            pass
        if visited.left:
            stack.append(visited.left)
        else:
            pass
    return count
