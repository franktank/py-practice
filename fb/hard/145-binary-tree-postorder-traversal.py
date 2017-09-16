"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        self.postorder_path = []
        self.postorder_iterative(root)
        self.postorder_path.reverse()
        return self.postorder_path

    def postorder(self, root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.postorder_path.append(root.val)

    def postorder_iterative(self, root):
        stack = list()
        stack.append(root)
        while stack:
            curr_node = stack.pop()
            self.postorder_path.append(curr_node.val)
            # reverse of preorder
            if curr_node.left:
                stack.append(curr_node.left)
            if curr_node.right:
                stack.append(curr_node.right)
