class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Find path with longest univalue
        self.max = 0
        self.helper(root)
        return self.max

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if root.left and root.left.val == root.val:
            left += 1
        else:
            left = 0

        if root.right and root.right.val == root.val:
            right += 1
        else:
            right = 0

        self.max = max(self.max, left + right)
        return max(left,right)
