"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.min_depth = sys.maxint
        self.find_min_depth(root)
        return self.min_depth

    def find_min_depth(self, node):
        if not node:
            return 0
        left_depth = self.find_min_depth(node.left)
        right_depth = self.find_min_depth(node.right)
        self.min_depth = min(min_depth, left_depth + 1, right_depth + 1) # +1 to include self
        return min(left_depth + 1, right_depth + 1)


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left == 0 or right == 0:
            return left + right + 1
        else:
            return 1 + min(left, right)
