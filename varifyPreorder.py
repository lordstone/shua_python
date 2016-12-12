class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if len(preorder) < 3: return True
        stack = [preorder[0]]
        minimum = - 0x7fffffff
        for i in range(1, len(preorder)):
            if preorder[i] < minimum: return False
            if len(stack) == 0: return False
            if preorder[i] < stack[len(stack) - 1]:
                stack.append(preorder[i])
            else:
                while stack and stack[len(stack) - 1] < preorder[i]:
                    minimum = stack[len(stack) - 1]
                    stack.pop()
                stack.append(preorder[i])
        return True

s = Solution()
arr = list(range(80))
print(str(s.verifyPreorder(arr)))

