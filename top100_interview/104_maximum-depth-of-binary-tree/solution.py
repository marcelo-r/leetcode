"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode, depth=0) -> int:
        if not root:
            return depth
        depth_left = self.maxDepth(root.left, depth+1)
        depth_right = self.maxDepth(root.right, depth+1)
        return max(depth_left, depth_right)

