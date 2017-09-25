# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.vals = []
        if root:
            self.inorder(root)


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.vals:
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        return self.vals.pop(0).val

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        self.vals.append(root)
        if root.right:
            self.inorder(root.right)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
