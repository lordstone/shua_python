# simgly linked list
import unittest


class LinkedListNode(object):
    def __init__(self, val=None, next_item=None):
        self.val = val
        self.next = next_item

    @staticmethod
    def produce(nodes):
        if not isinstance(nodes, list):
            return None
        prev = None
        for node_val in nodes[::-1]:
            node = LinkedListNode(node_val, prev)
            prev = node
        return prev

    @staticmethod
    def is_equal(a, b):
        if a is None or b is None:
            return a is None and b is None
        if a.val != b.val:
            return False
        return LinkedListNode.is_equal(a.next, b.next)

    def print(self):
        cur = self
        s = ''
        while cur:
            s += str(cur.val) + '->'
            cur = cur.next
        s += '(EOL)'
        print(s)


class Test(unittest.TestCase):
    def test_linkedlistnode(self):
        ln1 = LinkedListNode('a')
        ln2 = LinkedListNode('b')
        ln1.next = ln2
        self.assertEqual(ln1.val, 'a')
        self.assertEqual(ln2.val, 'b')
        self.assertEqual(ln1.next, ln2)
        self.assertEqual(ln1.next.val, 'b')

    def test_produce(self):
        ll1 = LinkedListNode.produce(['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(ll1.val, 'a')
        self.assertEqual(ll1.next.val, 'b')
        self.assertEqual(ll1.next.next.next.next.val, 'e')
        self.assertEqual(ll1.next.next.next.next.next, None)

    def test_isequal(self):
        ll1 = LinkedListNode.produce(['a', 'b', 'c', 'd', 'e'])
        ll2 = LinkedListNode.produce(['a', 'b', 'c', 'd', 'e'])
        ll3 = LinkedListNode.produce(['a', 'b', 'c', 'd'])
        self.assertEqual(LinkedListNode.is_equal(ll1, ll2), True)
        self.assertEqual(LinkedListNode.is_equal(ll1, ll3), False)
