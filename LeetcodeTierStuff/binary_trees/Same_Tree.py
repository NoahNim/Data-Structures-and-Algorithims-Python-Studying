# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Plan
# use deque to make a stack to do a dfs
# check if p.val equals q.val, if they do set you can pass, otherwise return False
# make a stack for p called p_stack
# make a stack for q called q_stack
# append each root to their stacks
# while p_stack and while q_stack
#   make a variable called p_visited equal to p_stack.pop()
#   make a variable called q_visited equal to q_stack.pop()
#   check if p_visited.right exists and q_visited.right exists
#       if they do check if their values are the same
#           if they are pass, else return False
#   check if p_visited.right and q.visited.right are both not None, if one of them is return False
#   check if p_visited.right exists if it does append it to p_stack else pass
#   check if q_visited.right exists if it does append it to q_stack else pass
#   repeat the steps done on right for the visited.left
# if the loop completes that means if found no mismatching values, and the function can return True
from collections import deque


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is not None and q is None:
            return False
        if p is None and q is not None:
            return False
        if p.val != q.val:
            return False
        p_stack = deque()
        q_stack = deque()
        q_stack.append(q)
        p_stack.append(p)
        while p_stack and q_stack:
            p_visited = p_stack.pop()
            q_visited = q_stack.pop()
            if p_visited.right and q_visited.right:
                if p_visited.right.val == q_visited.right.val:
                    pass
                else:
                    return False
            if p_visited.right is not None and q_visited.right is None:
                return False
            if p_visited.right is None and q_visited.right is not None:
                return False
            if p_visited.right:
                p_stack.append(p_visited.right)
            else:
                pass
            if q_visited.right:
                q_stack.append(q_visited.right)
            else:
                pass
            if p_visited.left and q_visited.left:
                if p_visited.left.val == q_visited.left.val:
                    pass
                else:
                    return False
            if p_visited.left is not None and q_visited.left is None:
                return False
            if p_visited.left is None and q_visited.left is not None:
                return False
            if p_visited.left:
                p_stack.append(p_visited.left)
            else:
                pass
            if q_visited.left:
                q_stack.append(q_visited.left)
            else:
                pass
        return True
