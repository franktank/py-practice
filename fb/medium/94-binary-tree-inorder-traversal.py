"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorder_path = []
        self.inorder(root)
        return self.inorder_path

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        self.inorder_path.append(root.val)
        self.inorder(root.right)

    def inorder_iterative(self, root):
        stack = list()
        curr_node = root
        while stack or curr_node:
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            curr_node = stack.pop()
            self.inorder_path.append(curr_node)
            curr_node = curr_node.right
