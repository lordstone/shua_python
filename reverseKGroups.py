# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def getLength(root):
            length = 0
            while root:
                length += 1
                root = root.next
            return length

        n = getLength(head)
        dummy = ListNode(-1)
        dummy.next = head
        root = dummy

        def revK(anchor, num):
            output = anchor.next
            cur, curNext = anchor.next, anchor.next.next
            while cur and cur.next and num > 1:
                future = curNext.next
                curNext.next = cur
                cur = curNext
                curNext = future
                num -= 1
            output.next = curNext
            anchor.next = cur
            return output

        while n // k > 0:
            root = revK(root, k)
            n -= k
        return dummy.next
