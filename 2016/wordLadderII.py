import collections


class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        if beginWord == endWord:
            return [beginWord]
        if len(wordlist) == 0:
            return []
        worddict = set(wordlist)
        pre_map = collections.defaultdict(set)
        prevStep = 0
        endStep = None
        curWords = [beginWord]
        nextWords = []

        while curWords:
            for i in curWords:
                if i in worddict:
                    worddict.discard(i)
            fe = False
            for cur in curWords:
                for i in range(len(cur)):
                    left, right = cur[:i], cur[i + 1:]
                    for rc in 'abcdefghijklmnopqrstuvwxyz':
                        if rc == cur[i]: continue
                        new_word = left + rc + right
                        if new_word == endWord or new_word in worddict:
                            pre_map[new_word].add(cur)
                            nextWords.append(new_word)
                            if new_word == endWord:
                                fe = True
            if fe: break
            if len(nextWords) == 0: return []

            curWords = nextWords[:]
            nextWords = []

        def build_res(pre_map, word, path, res):
            path.append(word)
            if len(pre_map[word]) == 0:
                tmp = path[:]
                tmp.reverse()
                res.append(tmp)
                path.pop()
                return
            for w in pre_map[word]:
                build_res(pre_map, w, path, res)
            path.pop()

        res = []
        build_res(pre_map, endWord, [], res)
        return res


s = Solution()
print(s.findLadders('hot', 'dog', ["hot","cog","dog","tot","hog","hop","pot","dot"]))
