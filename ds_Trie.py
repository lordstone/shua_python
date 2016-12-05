class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.endWord = None  # optional

    def look_up(self, letter):
        return self.children[ord(letter) - ord('a')]

    @staticmethod
    def build_trie(root, word):
        for c in word:
            if root.children[ord(c) - ord('a')] is None:
                root.children[ord(c) - ord('a')] = TrieNode()
            root = root.children[ord(c) - ord('a')]
        root.isEnd = True
        root.endWord = word  # optional
