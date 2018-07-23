# leetcode 825
# A will NOT request friend with B if any of the following is true
# age(B) <= 0.5 * age(A) + 7
# age(B) > age(A)
# age(B) > 100 && age(A) < 100
# how many friend requests will be there for a given age list
import unittest
from collections import Counter


class FriendsAges(object):
    def friends_request(self, people):
        if len(people) < 2:
            return 0
        ctr = dict(Counter(people))
        l = [[i, ctr[i]] for i in ctr]
        l.sort(key=lambda x: x[0])
        res = 0
        left = 0
        for i in range(len(l)):
            cur_age = l[i][0]
            num = l[i][1]
            bot = cur_age // 2 + 7
            while left < i and l[left][0] <= bot:
                left += 1
            res += (i - left) * num + num * (num - 1)
        return res


class Test(unittest.TestCase):
    def test_friendsrequest(self):
        target = FriendsAges()
        self.assertEqual(target.friends_request([16, 16]), 2)
        self.assertEqual(target.friends_request([16, 17, 18]), 2)
        self.assertEqual(target.friends_request([20, 30, 100, 110, 120]), 3)
