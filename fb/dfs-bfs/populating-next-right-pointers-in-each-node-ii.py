# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        parent = root
        start = None
        prev = None
        while parent:
            while parent:
                if parent.left:
                    if prev:
                        prev.next = parent.left
                    else:
                        head = parent.left
                    prev = parent.left
                if parent.right:
                    if prev:
                        prev.next = parent.right
                    else:
                        head = parent.right
                    prev = parent.right
                parent = parent.next
            parent = head
            head = None
            prev = None
