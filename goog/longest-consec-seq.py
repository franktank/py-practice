# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = 1
        prev_val = root.val
        self.helper(prev_val, 1, root.left)
        self.helper(prev_val, 1, root.right)
        return self.max

    def helper(self, prev_val, cur_count, node):
        if not node:
            return
        if node.val == prev_val + 1:
            cur_count += 1
            self.max = max(self.max, cur_count)
        else:
            cur_count = 1
        self.helper(prev_val, cur_count, root.left)
        self.helper(prev_val, cur_count, root.right)
