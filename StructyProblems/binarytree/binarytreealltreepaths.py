# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# make a depth first search recursion with a base of a leaf node (no right or left child) and a base of if the root is none
# make an empty list called paths
# make variables left_sub_paths and right_sub_paths that recursively call root.left and root.right
# after that loop through the lists that recursion ceeates, and append the value of root with the sub path lists to paths


def all_tree_paths(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [[root.val]]
    paths = []
    left_sub_paths = all_tree_paths(root.left)
    for sub_path in left_sub_paths:
        paths.append([root.val, *sub_path])
    right_sub_paths = all_tree_paths(root.right)
    for sub_path in right_sub_paths:
        paths.append([root.val, *sub_path])
    return paths
