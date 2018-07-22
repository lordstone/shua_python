class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def buildFromList(l):
    head = ListNode(-1)
    cur = head
    for i in l:
        cur.next = ListNode(i)
        cur = cur.next
    cur.next = None
    return head.next


def printList(head):
    s = ''
    while head is not None:
        s += str(head.val) + '->'
        head = head.next
    print(s)


# merge sort
def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    fast, slow = head, head
    while fast is not None and fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    def mergeTwo(l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        lcur = l1 if l2 is None else l2
        while lcur is not None:
            cur.next = lcur
            lcur = lcur.next
            cur = cur.next
        return dummy.next

    s2 = slow.next
    slow.next = None
    s1 = sortList(head)
    s2 = sortList(s2)
    start = mergeTwo(s1, s2)
    return start


h0 = buildFromList([1, 7, 4, 3, 7, 20, 7, 18, 50, -4, 3])
printList(h0)
hr0 = sortList(h0)
printList(hr0)
