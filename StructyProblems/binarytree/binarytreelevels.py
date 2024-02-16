# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# breath first search using queue
# empty list called tree_levels
# make a queue that starts with a tuple of root and 0
# while queue
# check if length of tree_levels list is equal to level_num, if so append node.val to tree_levels
# else append that node.val to levels[level_num]
# that check is checking the level number assigned to each node when added to the queue
# check if left and right exist, append each with level_num + 1 tuple
from collections import deque


def tree_levels(root):
    if root is None:
        return []
    tree_levels = []
    queue = deque([(root, 0)])
    while queue:
        node, level_num = queue.popleft()
        if len(tree_levels) == level_num:
            tree_levels.append([node.val])
        else:
            tree_levels[level_num].append(node.val)
        if node.left is not None:
            queue.append((node.left, level_num + 1))
        if node.right is not None:
            queue.append((node.right, level_num + 1))
    return tree_levels
