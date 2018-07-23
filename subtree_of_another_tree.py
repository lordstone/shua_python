# leetcode 572
import unittest
import time
from util.binary_tree import BinaryTreeNode


class Subtree(object):
    def is_subtree(self, s, t):
        # return if t is a subtree of s
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if self.is_same(s, t):
            return True
        else:
            return self.is_subtree(s.left, t) or self.is_subtree(s.right, t)

    def is_same(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val == t.val:
            return self.is_same(s.left, t.left) and self.is_same(s.right, t.right)
        else:
            return False


class Test(unittest.TestCase):
    def test_is_subtree(self):
        timer = time.time()
        s1 = BinaryTreeNode.produce([['a', 'b', 'c']])
        t1 = BinaryTreeNode.produce([['b']])
        t2 = BinaryTreeNode.produce([['d']])
        t3 = BinaryTreeNode.produce([['a', 'b']])
        subtree1 = Subtree()
        self.assertEqual(subtree1.is_subtree(s1, t1), True)
        self.assertEqual(subtree1.is_subtree(s1, t2), False)
        self.assertEqual(subtree1.is_subtree(s1, t3), False)
        s2 = BinaryTreeNode.produce([['a', 'b', 'c'], ['b', 'd', 'e'], ['c', 'f', 'g'],
                                     ['d', 'h', 'i'], ['e', 'e1', 'e2'], ['f', 'f1', 'f2'],
                                     ['g', 'g1', 'g2'], ['h', 'h1', 'h2'], ['i', 'i1', 'i2'],
                                     ['e1', 'e3'], ['e2', None, 'e4'], ['f1', None, 'f3']])
        t4 = BinaryTreeNode.produce([['e1', 'a']])
        t5 = BinaryTreeNode.produce([['e1', 'e3']])
        self.assertEqual(subtree1.is_subtree(s2, t4), False)
        self.assertEqual(subtree1.is_subtree(s2, t5), True)
        t = time.time() - timer
        self.assertGreater(1, t, 'operation timeout!')  # less than 1 s is allowed
