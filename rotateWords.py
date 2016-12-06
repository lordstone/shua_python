class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
        fast, slow = 0, 0
        while fast <= len(s) and slow < len(s):
            while fast < len(s) and s[fast] != ' ':
                fast += 1
            for i in range((fast - slow) // 2):
                s[i + slow], s[fast - i - 1] = s[fast - i - 1], s[i + slow]
            while fast < len(s) and s[fast] == ' ':
                fast += 1
            slow = fast


s = Solution()
st = list('   hello world jiji  123   ')
s.reverseWords(st)
print(''.join(st))
