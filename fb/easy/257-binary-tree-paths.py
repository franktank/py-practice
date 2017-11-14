"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS Solution
import Queue
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # Find all paths
        # Track leaves -> nodes with no children
        # Return path to leaves
        if not root:
            return list()
        self.parents = {}
        self.leaves = []
        self.find_all_paths(root)
        return self.path_to_leaves()

    def find_all_paths(self, node):
        q = Queue.Queue()
        q.put(node)
        self.parents[node] = None
        while not q.empty():
            curr_node = q.get()
            if not curr_node.left and not curr_node.right:
                self.leaves.append(curr_node)
            if curr_node.left:
                q.put(curr_node.left)
                self.parents[curr_node.left] = curr_node
            if curr_node.right:
                q.put(curr_node.right)
                self.parents[curr_node.right] = curr_node

    def path_to_leaves(self):
        path_to_leaves = list()
        for leaf in self.leaves:
            path = str(leaf.val)
            curr_node = self.parents[leaf]
            while curr_node:
                path = str(curr_node.val) + '->' + path
                curr_node = self.parents[curr_node]
            path_to_leaves.append(path)
        return path_to_leaves

# BFS Solution
import Queue
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # Find all paths
        # Track leaves -> nodes with no children
        # Return path to leaves
        if not root:
            return list()
        self.paths = []
        self.find_all_paths(root)
        return self.paths

    def find_all_paths(self, node):
        q = []
        q.append((node, str(node.val)))
        while q:
            curr_node = q.pop(0)
            print(curr_node)
            if not curr_node[0].left and not curr_node[0].right:
                self.paths.append(curr_node[1])
            if curr_node[0].left:
                q.append((curr_node[0].left, curr_node[1] + '->' + str(curr_node[0].left.val)))
            if curr_node[0].right:
                q.append((curr_node[0].right, curr_node[1] + '->' + str(curr_node[0].right.val)))

# DFS Solution
# Preorder
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return list()
        self.path_to_leaves = []
        self.dfs(root, '')
        return self.path_to_leaves

    def dfs(self, root, current_path):
        if not root.left and not root.right:
            self.path_to_leaves.append(current_path + str(root.val))
        if root.left:
            self.dfs(root.left, current_path + str(root.val) + '->')
        if root.right:
            self.dfs(root.right, current_path + str(root.val) + '->')
