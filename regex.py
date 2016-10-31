
def match(s, pattern):
    if s is None or pattern is None:
        return False
    if s == "" and pattern == "":
        return True
    elif s == "" and pattern != "":
        return False
    if s != "" and pattern == "":
        return False

    if len(pattern) > 1 and pattern[1] == '*':
        if pattern[0] == s[0] or (pattern[0] == '.' and len(s) > 0):
            return match(s[1:], pattern[2:]) \
                   or match(s[1:], pattern) \
                   or match(s, pattern[2:])
        else:
            return match(s, pattern[2:])

    if s[0] == pattern[0] or (pattern[0] == '.' and len(s) > 0):
        return match(s[1:], pattern[1:])

    return False

print(match("aaa", "aaaa"))

