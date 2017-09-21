"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return list()
        self.verticals = {}
        self.bfs(root)
        print(self.verticals)
        a = list(self.verticals.keys())
        a.sort()
        ret_list = []
        for element in a:
            ret_list.append(self.verticals[element])
        return ret_list

    def bfs(self, root):
        q = []
        col = 0
        q.append((root, col))
        self.verticals[col] = [root.val]
        while q:
            curr_tuple = q.pop(0)
            curr_node = curr_tuple[0]
            curr_col = curr_tuple[1]
            # put in left
            if curr_node.left:
                q.append((curr_node.left, curr_col-1))
                if curr_col-1 in self.verticals:
                    self.verticals[curr_col-1].append(curr_node.left.val)
                else:
                    self.verticals[curr_col-1] = [curr_node.left.val]
            if curr_node.right:
                q.append((curr_node.right, curr_col+1))
                if curr_col+1 in self.verticals:
                    self.verticals[curr_col+1].append(curr_node.right.val)
                else:
                    self.verticals[curr_col+1] = [curr_node.right.val]

"""
Create dictionary that maps:
    Column => Node Values
Root is column 0, left is column - 1, right is column + 1
BFS, Queue store a tuple (node, column)
At each tuple, handle left and right child
    If curr_col - 1 is in dictionary, append, else create [curr_node.left]
    If curr_col + 1 is in diciionary, append, else create [curr_node.right]
After BFS
Get keys, sort
Use sorted keys to create return list
"""
