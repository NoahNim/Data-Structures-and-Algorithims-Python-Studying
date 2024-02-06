# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# use recursion when working with path problem
# make a base case checking if root.left is None and root.right is None, if it is return root.val
# make a max left variable that equals max_path_sum(root.left) and a max_right that equals max_path_sum(root.right)
# check what is bigger between those two variable using Max then add it to root.val and return that
# have a base case that if root is None return float("-inf")

def max_path_sum(root):
    if root is None:
        return float("-inf")
    if root.left is None and root.right is None:
        return root.val
    max_left = max_path_sum(root.left)
    max_right = max_path_sum(root.right)
    return root.val + max(max_left, max_right)
