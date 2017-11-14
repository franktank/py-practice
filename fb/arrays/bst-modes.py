# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.modes = []
        self.mode_len = 0
        self.cur_len = 0
        self.cur_ele = None
        return self.modes
        
    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        if not self.cur_ele == root.val:
            if self.cur_len == self.mode_len
                self.modes.append(self.cur_ele)
            elif self.cur_len > self.mode_len
                self.mode_len = self.cur_len
                self.modes = [self.cur_ele]
            self.cur_len = 1
            self.cur_ele = root.val
        else:
            self.cur_len += 1
        if root.right:
            self.inorder(root.right)
