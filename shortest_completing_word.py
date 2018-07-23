# leetcode 748
import unittest
import collections


class CompletingWord(object):
    def find(self, target, words):
        ctr = collections.Counter(filter(str.isalpha, target.lower()))
        length = sum(ctr.values())
        d = dict(ctr)
        best = None
        for i, word in enumerate(words):
            if len(word) < length or (best is not None and len(word) >= len(words[best])):
                continue
            dd = d.copy()
            for c in word:
                if c in dd:
                    dd[c] -= 1
                    if dd[c] == 0:
                        del dd[c]
            if len(dd) == 0:
                best = i
        return words[best] if best is not None else None


class Test(unittest.TestCase):
    def test_find(self):
        target = CompletingWord()
        self.assertEqual(target.find('1s3 PSt', ["step", "steps", "stripe", "stepple"]), 'steps')
        self.assertEqual(target.find("1s3 456", ["looks", "pest", "stew", "show"]), 'pest')
        self.assertEqual(target.find("OgEu755",
                                     ["enough", "these", "play", "wide", "wonder", "box",
                                      "arrive", "money", "tax", "thus"]), 'enough')
