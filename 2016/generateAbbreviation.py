def generateAbbreviations(word):
    dp = dict()
    def gen(start, end):
        if (start, end) in dp:
            return dp[(start, end)]
        if start >= end:
            return []
        tmpres = set()
        for i in range(start, end + 1):
            prefix = []
            if i >= 0:
                prefix.append(word[start:i + 1])
                prefix.append(str(i + 1 - start))
            else:
                prefix.append('')
            suffix = gen(i + 1, end)
            for i in prefix:
                for j in suffix:
                    if i[-1].isdigit() and j[0].isdigit():
                        continue
                    tmpres.add(i + j)
        tmpres.add(word[start:end + 1])
        tmpres.add(str(len(word[start:end + 1])))
        dp[(start, end)] = tmpres
        return tmpres
    return list(gen(0, len(word)))


s = 'multiplication'
print(generateAbbreviations(s))
