import unittest
import time


class Regex(object):
    cache = dict()

    @staticmethod
    def match_nocache(s, p):
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) == 0:
            return True if len(p) == 2 and p[1] == '*' else False
        if len(p) == 0:
            return False
        if len(p) > 1 and p[1] == '*':
            if p[0] == '.' or p[0] == s[0]:
                return Regex.match(s, p[2:]) or Regex.match(s[1:], p)
            else:
                return Regex.match(s, p[2:])
        else:
            if p[0] == '.':
                return Regex.match(s[1:], p[1:])
            else:
                return s[0] == p[0] and Regex.match(s[1:], p[1:])

    @staticmethod
    def match(s, p):
        if s + ':' + p in Regex.cache:
            return Regex.cache[s + ':' + p]
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) == 0:
            if len(p) >= 2 and p[1] == '*':
                Regex.cache[s + ':' + p] = Regex.match(s, p[2:])
                return Regex.cache[s + ':' + p]
            else:
                return False
        if len(p) == 0:
            return False
        if len(p) > 1 and p[1] == '*':
            if p[0] == '.' or p[0] == s[0]:
                Regex.cache[s + ':' + p] = Regex.match(s, p[2:]) or Regex.match(s[1:], p)
            else:
                Regex.cache[s + ':' + p] = Regex.match(s, p[2:])
        else:
            if p[0] == '.':
                Regex.cache[s + ':' + p] = Regex.match(s[1:], p[1:])
            else:
                Regex.cache[s + ':' + p] = (s[0] == p[0] and Regex.match(s[1:], p[1:]))
        return Regex.cache[s + ':' + p]


class Test(unittest.TestCase):
    def test_regex(self):
        timer = time.time()
        self.assertEqual(Regex.match('abcde', 'as'), False)
        self.assertEqual(Regex.match('abcde', 'a...e'), True)
        self.assertEqual(Regex.match('abcde', 'a..d.'), True)
        self.assertEqual(Regex.match('abcde', 'ab*c*e*d.'), True)
        self.assertEqual(Regex.match('abcde', 'a.*'), True)
        self.assertEqual(Regex.match('abcde', 'a.*a'), False)
        self.assertEqual(Regex.match("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"), False)
        self.assertEqual(Regex.match('', '.*c*'), True)
        self.assertEqual(Regex.match('aa', 'a*'), True)
        t = time.time() - timer
        self.assertGreater(1, t, 'operation timeout!')  # less than 1 s is allowed
