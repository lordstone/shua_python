# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def swap(x, y):
    x.val, y.val = y.val, x.val


def traverse_cmp(root, batch):
    [p1, p2, prev] = batch
    if root.left:
        [p1, p2, prev] = traverse_cmp(root.left, [p1, p2, prev])
    if prev and prev.val > root.val:
        if not p1:
            p1 = prev
        if p1:
            p2 = root
    prev = root
    if root.right:
        [p1, p2, prev] = traverse_cmp(root.right, [p1, p2, prev])
    return [p1, p2, prev]


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        p1, p2, prev = None, None, None
        [p1, p2, prev] = traverse_cmp(root, [p1, p2, prev])
        if p1 and p2:
            swap(p1, p2)
