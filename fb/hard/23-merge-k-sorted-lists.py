class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists) > 1:
            next_list = list()
            i = 0
            while i < len(lists):
                if i == len(lists) - 1:
                    next_list.append(lists[i])
                    i += 1
                else:
                    next_list.append(self.merge(list_a, list_b))
                    i += 2
            lists = list(next_list)

        if lists:
            return lists[0]
        else:
            return None

    def merge(self, list_a, list_b):
        head = merged_list = ListNode(0)
        while list_a or list_b:
            if not list_a:
                merged_list.next = list_b
                break
            if not list_b:
                merged_list.next = list_a
                break
            if list_a.val > list_b.val:
                merged_list.next = list_b
                merged_list = merged_list.next
                list_b = list_b.next
            elif list_a.val <= list_b.val:
                merged_list.next = list_a
                merged_list = merged_list.next
                list_a = list_a.next

        return head.next
