"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
import Queue

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS with an index, when 0 -> new level?
        if root == None:
            return list()
        current_level = 1
        new_level = 0

        q = Queue.Queue()
        q.put(root)

        ret_list = list()
        curr_list = list()
        while not q.empty():
            curr_node = q.get()
            curr_list.append(curr_node.val)
            if curr_node.left:
                q.put(curr_node.left)
                new_level += 1
            if curr_node.right:
                q.put(curr_node.right)
                new_level += 1

            current_level -= 1
            if current_level == 0:
                current_level = int(new_level)
                new_level = 0
                ret_list.append(curr_list)
                curr_list = list()

        return ret_list
