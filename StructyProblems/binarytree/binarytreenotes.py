# a tree is a co0llection of branches with nodes
# a node can be a parent with children node, a node with no parent is the root
# a leaf node is a node with zero children
# a binary tree is a tree where every node has at least two children
# exactly one path between root and any node
# think of a tree with only an a and b nodes, it's still bonary, same with just one node or no nodes (an empty tree)
# Binary Tree:
#           A
#         /   \
#        B     C
#       /\      \
#     D   E      F

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.left = e
c.right = f
