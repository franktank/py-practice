# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = 0
        self.helper(root, root.val)

    def helper(self, root, prev):
        if root.val != prev:
            return 0
        left = 1 + self.helper(root.left, root.val)
        right = 1 + self.helper(root.right, root.val)
        self.max = max(self.max, left+right)
        return max(left,right)
