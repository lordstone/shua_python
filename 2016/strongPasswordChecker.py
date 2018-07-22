class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        prev = None
        prevcnt = short = excess = 0
        lack_digits = lack_lower = lack_upper = 1
        repcnt = 0
        length = len(s)
        if length > 20:
            excess = length - 20
        elif length < 6:
            short = 6 - length

        for c in s:
            if prev and prev == c:
                prevcnt += 1
                if prevcnt >= 2:
                    prev = None
                    repcnt += 1
                    prevcnt = 0
            else:
                prevcnt = 0
                prev = c
            if c.isdigit():
                lack_digits = 0
            elif c.islower():
                lack_lower = 0
            elif c.isupper():
                lack_upper = 0
        lacks = lack_digits + lack_lower + lack_upper
        return max(short, excess, repcnt, lacks)

