# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# use a breadth first search
# make a variable called most_right
# use deque make a queue that has root in it
# while the queue exists put each node that exist as most_right, it will eventually put the node furthest on the right of the tree in the most_right variable
# return most right
from collections import deque


def bottom_right_value(root):
    if root.right is None and root.left is None:
        return root.val
    most_right = root.right.val
    queue = deque()
    queue.append(root)
    while queue:
        visited = queue.popleft()
        if visited.left:
            queue.append(visited.left)
            most_right = visited.left.val
        else:
            pass
        if visited.right:
            queue.append(visited.right)
            most_right = visited.right.val
        else:
            pass
    return most_right
