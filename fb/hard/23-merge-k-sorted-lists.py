class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists) > 1:
            next_list = list()
            leftovers = 0
            for i in range(1, len(lists), 2):
                list_a = lists[i-1]
                list_b = lists[i]
                m = self.merge(list_a, list_b)
                next_list.append(m)
                leftovers = i
            if (i < len(lists) - 1):
                # If odd size list, we will have leftovers from before
                for j in range(i + 1, len(lists)):
                    next_list.append(lists[j])
            lists = list(next_list)

        if lists:
            return lists[0]
        else:
            return lists

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
