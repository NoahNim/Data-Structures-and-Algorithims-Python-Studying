# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# take in root of binary tree
# if node doesn't have left or right child, those become null/None
# if doing a depth first traversal, you go deeper in the tree then go laterally from there
# use a Stack, a sequential data structure where you can only add things to the top of the stack and remove from the top of the stack
# store root node in stack
# check if stack is empty in loop
# remove the top element and consider it visited, look at that nodes children
# add the children to the stack (if they exist), (if) right first then (if) left second (so left becomes top of stack)
# when you reach a child with no children, pop that from the stack then go to the next in the stack and see if it has children, otherwrise pop it
# when somethiong leaves the stack, add it to a values variabloe to list them
from collections import deque


def depth_first_values(root):
    if root is None:
        return []
    values = []
    stack = deque()
    stack.append(root)
    while stack:
        visited = stack.pop()
        values.append(visited.val)
        if visited.right:
            stack.append(visited.right)
        else:
            pass
        if visited.left:
            stack.append(visited.left)
        else:
            pass
    return values
