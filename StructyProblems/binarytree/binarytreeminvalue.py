# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque


def tree_min_value(root):
    if root is None:
        return None
    min_value = root.val
    stack = deque()
    stack.append(root)
    while stack:
        visited = stack.pop()
        if visited.val < min_value:
            min_value = visited.val
        if visited.right:
            stack.append(visited.right)
        else:
            pass
        if visited.left:
            stack.append(visited.left)
        else:
            pass
    return min_value
