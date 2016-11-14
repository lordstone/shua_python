class Solution(object):

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None:
            return
        if node.next is None:
            del node
        else:
            while node.next and node.next.next:
                node.val = node.next.val
                node = node.next
            node.val = node.next.val
            del node.next
            node.next = None
