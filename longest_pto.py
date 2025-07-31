
# https://www.1point3acres.com/bbs/thread-1138978-1-1.html
def find_longest_pto(cal: str, pto: int) -> int:
    """
    This function finds the longest PTO days with the given calendar string and PTO allowance.
    'w' is a workday, 'h' is a holiday.
    """
    best = 0
    start = 0


    for idx, s in enumerate(cal):
        assert s in 'wh', "Invalid character in calendar string. Only 'w' and 'h' are allowed."
        if s == 'h':
            continue
        if s == 'w':
            if pto > 0:
                pto -= 1
                continue
            best = max(best, idx - start)
            while start < idx and cal[start] == 'h':
                start += 1
            if cal[start] == 'w':
                start += 1
            
    return max(best, len(cal) - start)


def assert_and_print(actual_res: int, exp_res: int):
    if actual_res != exp_res:
        print(f"actual result: {actual_res}, expected result: {exp_res}")


def main():
    assert_and_print(find_longest_pto('whhwhww', 0), 2)
    assert_and_print(find_longest_pto('whhwhww', 1), 4)
    assert_and_print(find_longest_pto('whhwhww', 2), 5)
    assert_and_print(find_longest_pto('whhwhwhhww', 2), 7)
    assert_and_print(find_longest_pto('whhhwwhhww', 2), 7)


if __name__ == "__main__":
    main()
