# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# check if root is None if so return 0
# create a queue
# create a variable levels that's an empty list
# append a set of (node: root, level: 0)
# do a while loop while queue
# # make a variable visited equal to stack.pop
# # make a variable current equal to visited.node
# # check if length of levels is less than visited.level if it is append visited to levels
# # check if current.left exists, if so append a set of ( node: current.left, level: len(levels) )
# # check if current.right exists, if so append a set of ( node: current.right, level: len(levels) )
# return the length ofd levels
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([])
        levels = [root.val]
        queue.append((root, 1))
        while queue:
            visited = queue.popleft()
            current = visited[0]
            if visited[1] > len(levels):
                levels.append(current.val)
            if current.left:
                queue.append((current.left, len(levels) + 1))
            else:
                pass
            if current.right:
                queue.append((current.right, len(levels) + 1))
            else:
                pass
        return len(levels)