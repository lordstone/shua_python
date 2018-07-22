import bisect


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap, res = [], ListNode(-1)
        cur = res
        for idx, l in enumerate(lists):
            if l:
                bisect.insort(heap, (l.val, idx))
        while heap:
            v, idx = heap.pop(0)
            cur.next = ListNode(v)
            cur = cur.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                bisect.insort(heap, (lists[idx].val, idx))
        return res.next
