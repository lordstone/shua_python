# leetcode 623
import unittest
from util.binary_tree import BinaryTreeNode


class AddRow(object):
    def add_row(self, root, v, d, is_right=False):
        if d == 1:
            node = BinaryTreeNode(v)
            if is_right:
                node.right = root
            else:
                node.left = root
            return node
        elif root is None:
            return None
        elif d == 2:
            root.left, root.right = self.add_row(root.left, v, 1), self.add_row(root.right, v, 1, True)
        else:
            root.left, root.right = self.add_row(root.left, v, d-1), self.add_row(root.right, v, d-1)
        return root


class Test(unittest.TestCase):
    def test_addrow(self):
        target = AddRow()
        bt1 = BinaryTreeNode.produce([[1, 2, 3]])
        ans1 = BinaryTreeNode.produce([[4, 1], [1, 2, 3]])
        res1 = target.add_row(bt1, 4, 1)
        self.assertEqual(BinaryTreeNode.compare(res1, ans1), True)
        bt2 = BinaryTreeNode.produce([[1, 2, 3]])
        ans2_leaf_left = BinaryTreeNode.produce([[4, 2]])
        ans2_leaf_right = BinaryTreeNode.produce([[4, None, 3]])
        ans2 = BinaryTreeNode(1, ans2_leaf_left, ans2_leaf_right)
        res2 = target.add_row(bt2, 4, 2)
        self.assertEqual(BinaryTreeNode.compare(res2, ans2), True)
        bt3 = BinaryTreeNode.produce([[1, 2, 3]])
        ans3_leaf_left = BinaryTreeNode.produce([[2, 4, 4]])
        ans3_leaf_right = BinaryTreeNode.produce([[3, 4, 4]])
        ans3 = BinaryTreeNode(1, ans3_leaf_left, ans3_leaf_right)
        res3 = target.add_row(bt3, 4, 3)
        self.assertEqual(BinaryTreeNode.compare(res3, ans3), True)
