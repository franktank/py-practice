"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # BFS to find node
        trv = t.val
        q = []
        q.append(s)
        st_node = None
        while q:
            cur = q.pop(0)
            if cur.val == trv:
                st_node = cur
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        tpo = []
        self.preorder(st_node, tpo)
        spo = []
        self.preorder(s, spo)
        return rpo == spo

    def preorder(self, root, po):
        po.append(root.val)
        if root.left:
            preorder(root.left, po)
        if root.right:
            preorder(root.right, po)

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None: # Basically couldn't find a subtree
            return False
        if self.is_same(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same(self, s, t):
        if (not s.val == t.val):
            return False
        if s.val == t.val and not s.left and not t.left and not s.right and not t.right:
            return True
        return is_same(s.left, t.left) and is_same(s.right, t.right)
