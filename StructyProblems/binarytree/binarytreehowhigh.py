# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# use recurion
# split each tree in half with recursive calls, right_height and left_height
# in each branch do 1 + the recursion
# return 0 in those recursions if node is None
# check if those nodes node.right or node.left exists
# if they do return 1 + _how_high(node.right) + _ how_high(node.left)
# return the variable with the larger number of the comparison between left_height and right_height

def how_high(node):
    if node is None:
        return -1
    if node.right is None and node.left is None:
        return 0
    left_height = 1 + _how_high(node.left)
    right_height = 1 + _how_high(node.right)
    if right_height > left_height:
        return right_height
    elif left_height > right_height:
        return left_height
    else:
        return right_height


def _how_high(node):
    if node is None:
        return 0
    print(node.val)
    if node.right is None and node.left is None:
        return 0
    elif node.right or node.left:
        return 1 + _how_high(node.right) + _how_high(node.left)
