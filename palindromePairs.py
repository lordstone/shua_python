class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(word):
            size = len(word)
            for x in range(size / 2):
                if word[x] != word[size - x - 1]:
                    return False
            return True
        wmap = dict()
        for idx, word in enumerate(words):
            wmap[word] = idx
        res = set()
        for idx, word in enumerate(words):
            if word == '':
                continue
            if isPalindrome(word):
                if '' in wmap:
                    res.add((wmap[''], idx))
                    res.add((idx, wmap['']))
            if word[::-1] in wmap:
                if wmap[word[::-1]] != idx:
                    res.add((wmap[word[::-1]], idx))
                    res.add((idx, wmap[word[::-1]]))
            for x in range(1, len(word)):
                left, right = word[:x], word[x:]
                if isPalindrome(left) and right[::-1] in wmap:
                    res.add((wmap[right[::-1]], idx))
                if isPalindrome(right) and left [::-1] in wmap:
                    res.add((idx, wmap[left[::-1]]))
        return list(res)