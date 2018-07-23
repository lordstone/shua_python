# leetcode 83
import unittest
from util.linked_list import LinkedListNode


class RemoveDuplicate(object):
    def remove(self, node):
        if node is None:
            return
        cur = node
        while cur:
            nextone = cur.next
            while nextone and nextone.val == cur.val:
                nextone = nextone.next
            cur.next = nextone
            cur = nextone


class Test(unittest.TestCase):
    def test_removeduplicate(self):
        ll1 = LinkedListNode.produce([1, 1, 2, 2, 3, 3, 3, 3, 4, 4,
                                      5, 6, 7, 8, 9, 9])
        ll1_golden = LinkedListNode.produce([1, 2, 3, 4, 5, 6, 7, 8, 9])
        target = RemoveDuplicate()
        target.remove(ll1)
        ll1.print()
        self.assertEqual(LinkedListNode.is_equal(ll1, ll1_golden), True)

