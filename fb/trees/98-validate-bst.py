# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.io = []
        self.inorder(root)
        for i in range(1, len(self.io)):
            if self.io[i-1] >= self.io[i]:
                return False
        return True

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)

        self.io.append(root.val)

        if root.right:
            self.inorder(root.right)
