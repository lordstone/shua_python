def  check_log_history( events):
    stack = []
    cache = set()
    for idx, s in enumerate(events):
        action, num = s.split(' ')
        if action == 'ACQUIRE':
            if num not in cache:
                cache.add(num)
                stack.append(num)
            else:
                return idx + 1
        else:
            if num in cache:
                if stack[-1] == num:
                    cache.discard(num)
                    stack.pop(-1)
                else:
                    return idx + 1
            else:
                return idx + 1
    if len(cache) > 0:
        return len(cache) + 1
    else:
        return 0


