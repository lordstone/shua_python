class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    @staticmethod
    def build_trie(root, word):
        for c in word:
            if root.children[ord(c) - ord('a')] is None:
                root.children[ord(c) - ord('a')] = TrieNode()
            root = root.children[ord(c) - ord('a')]
        root.isEnd = True
