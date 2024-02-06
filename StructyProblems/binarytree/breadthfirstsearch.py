# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# breadth first traversal means you travel across, not down like in a depth first search
# breadth first uses a queue instead of a stack, so first out last in
# check if queue is empty
# make a variable called visited inside a while loop while queue is not empty
# add its children to the queue, left to right

from collections import deque


def breadth_first_values(root):
    if root is None:
        return []
    values = []
    queue = deque()
    queue.append(root)

    while queue:
        visited = queue.popleft()
        values.append(visited.val)
        if visited.left:
            queue.append(visited.left)
        else:
            pass
        if visited.right:
            queue.append(visited.right)
        else:
            pass
    return values
