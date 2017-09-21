"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # Do a good level order traversal
        q = []
        q.append(root)
        avg = []
        level_count = 1
        while q:
            next_level_count = 0
            curr_sum = 0
            curr_avg = 0
            for i in range(level_count):
                curr_node = q.pop(0)
                curr_sum += curr_node.val
                if curr_node.left:
                    q.append(curr_node.left)
                    next_level_count += 1
                if curr_node.right:
                    q.append(curr_node.right)
                    next_level_count += 1
            curr_avg = float(curr_sum) / float(level_count)
            avg.append(curr_avg)
            level_count = int(next_level_count)
        return avg

"""
BFS
For loop to iterate through each level
Indices to track size of current level and size of next level
"""
