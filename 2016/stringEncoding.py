class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        p0, p1 = 0, 0
        rstr = ""
        while p0 < len(strs):
            if p1 < len(strs[p0]):
                if strs[p0][p1] == 'x':
                    rstr += 'x'
                rstr += strs[p0][p1]
                p1 += 1
            if p1 == len(strs[p0]):
                p0 += 1
                p1 = 0
                rstr += 'x0'
        return rstr

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        res, cur = [], ""
        p = 0
        while p < len(s):
            if p < len(s) - 1:
                if s[p] == 'x':
                    p += 1
                    if s[p] == '0':
                        res.append(cur)
                        cur = ""
                        p += 1
                        continue
            cur += s[p]
            p += 1
        return res


strs = ['', '123', '123213', '', 'xxxxx0x0x0x0xxxxx0x0x00xxx0x0x']
codec = Codec()
print(codec.decode(codec.encode(strs)))