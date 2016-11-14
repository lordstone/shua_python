def wordBreak(word, dictionary):
    if len(word) < 2:
        return []
    dp, res = [-1] * len(word), []
    for i in range(len(word)):
        for j in range(i+1):
            if word[j:i+1] in dictionary and (j == 0 or dp[j-1] != -1):
                dp[i] = j-1 if j != 0 else -2
                break
    if dp[len(word)-1] == -1:
        return []
    cur = len(word)-1
    while dp[cur] != -2:
        res.append(word[dp[cur]+1:cur+1])
        cur = dp[cur]
    res.append(word[:cur+1])
    res.reverse()
    return res


dictionary = {'abc', 'def', 'ghjk'}
s = 'abcdefghjk'
print(wordBreak(s, dictionary))
