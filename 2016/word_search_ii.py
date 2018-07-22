class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.endWord = None

    def look_up(self, letter):
        return self.children[ord(letter) - ord('a')]

    @staticmethod
    def build_trie(root, word):
        for c in word:
            if root.children[ord(c) - ord('a')] is None:
                root.children[ord(c) - ord('a')] = TrieNode()
            root = root.children[ord(c) - ord('a')]
        root.isEnd = True
        root.endWord = word


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        n = len(board)
        m = 0 if n == 0 else len(board[0])
        if m == 0 or len(words) == 0: return []

        res = set()
        root = TrieNode()
        for w in words:
            TrieNode.build_trie(root, w)

        def dfs(cx, cy, anchor, res, cset):
            next_node = anchor.look_up(board[cx][cy])
            if next_node:
                if next_node.isEnd:
                    res.add(next_node.endWord)
                    next_node.isEnd = False
                    # return
                cset.add((cx, cy))
                for dx, dy in directions:
                    x, y = cx + dx, cy + dy
                    if x >= n or x < 0 or y >= m or y < 0 or (x, y) in cset:
                        continue
                    dfs(x, y, next_node, res, cset.copy())
                cset.discard((cx, cy))

        for i in range(n):
            for j in range(m):
                dfs(i, j, root, res, set())

        res = list(res)
        res.sort()
        return res


s = Solution()
input1 = ["ab", "aa", "ac"]
input2 = ["aba", "abaa", "abaca"]
print(s.findWords(input1, input2))

