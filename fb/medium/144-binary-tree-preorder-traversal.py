"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.preorder_path = list()
        self.preorder_iterative(root)
        return self.preorder_path

    def preorder(self, root):
        if root == None:
            return
        self.preorder_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorder_iterative(self, root):
        # DFS
        stack = list()
        stack.append(root)
        while stack:
            curr_node = stack.pop()
            self.preorder_path.append(curr_node.val)
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left: # this is last because want to explore left first!
                stack.append(curr_node.left)
