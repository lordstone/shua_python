# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


INT_MIN = -0x7fffffff


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def retBestCur(node):
            if not node:
                return INT_MIN, INT_MIN
            if (not node.left) and (not node.right):
                return node.val, node.val
            lbest, lcur = retBestCur(node.left)
            rbest, rcur = retBestCur(node.right)
            cross = max(lcur + node.val + rcur, node.val + rcur, node.val + lcur, node.val)
            return max(cross, max(lbest, rbest)), max(max(lcur, rcur) + node.val, node.val)

        best, cur = retBestCur(root)
        return best
