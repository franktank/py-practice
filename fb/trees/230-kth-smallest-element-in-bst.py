# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.inorder(root)
        return self.kth_element

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)

        self.k -= 1
        if self.k == 0:
            self.kth_element = root.val

        if root.right:
            self.inorder(root.right)
