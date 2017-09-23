"""
Reverse a singly linked list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
[1] -> [2] -> [3]

[1]
rev_list

[2] -> [1]
rev_list

[3] -> [2] -> [1]
rev_list
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        rev_list = head
        curr_head = head.next
        rev_list.next = None
        while curr_head:
            temp = curr_head.next
            curr_head.next = rev_list
            rev_list = curr_head
            curr_head = temp
        return rev_list
