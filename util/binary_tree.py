import unittest


class BinaryTreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def produce(ls):
        # ls is list of nodes, where an element has 1 to 3 str, for parent node, left node, and right node
        # return the first node
        nodemap = dict()
        head = ls[0][0]
        for node in ls:
            parent = node[0]
            left = None if len(node) < 2 else node[1]
            right = None if len(node) < 3 else node[2]
            for cur in (parent, left, right):
                if cur not in nodemap:
                    nodemap[cur] = BinaryTreeNode(cur)
            if left:
                nodemap[parent].left = nodemap[left]
            if right:
                nodemap[parent].right = nodemap[right]
        return nodemap[head]


class Test(unittest.TestCase):
    def test_binarytreenode_init(self):
        t1 = BinaryTreeNode()
        self.assertEqual(t1.val, None)
        self.assertEqual(t1.left, None)
        self.assertEqual(t1.right, None)
        t2 = BinaryTreeNode('abc')
        self.assertEqual(t2.val, 'abc')
        self.assertEqual(t2.left, None)
        self.assertEqual(t2.right, None)
        t3 = BinaryTreeNode('11', t1, t2)
        self.assertEqual(t3.val, '11')
        self.assertEqual(t3.left, t1)
        self.assertEqual(t3.right, t2)
        self.assertEqual(t3.left.val, None)
        self.assertEqual(t3.right.val, 'abc')

    def test_binarytreenode_produce(self):
        t1 = BinaryTreeNode.produce([['a', 'b'], ['b', 'c', 'd'], ['c', None, 'e'], ['d', 'f']])
        self.assertNotEqual(t1, None)
        self.assertEqual(t1.val, 'a')
        self.assertEqual(t1.left.val, 'b')
        self.assertEqual(t1.right, None)
        self.assertEqual(t1.left.left.val, 'c')
        self.assertEqual(t1.left.right.val, 'd')
        self.assertEqual(t1.left.left.left, None)
        self.assertEqual(t1.left.left.right.val, 'e')
        self.assertEqual(t1.left.right.left.val, 'f')
