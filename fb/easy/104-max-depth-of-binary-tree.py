"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max_depth = -1
        self.find_max_depth(root)
        return self.max_depth

    def find_max_depth(self, node):
        if not node:
            return 0
        left_depth = self.find_max_depth(node.left)
        right_depth = self.find_max_depth(node.right)
        self.max_depth = max(self.max_depth, left_depth + 1, right_depth + 1) # +1 to include self?
        return max(left_depth + 1, right_depth + 1)
