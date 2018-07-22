import time


def test_fib():

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return fib(n - 1) + fib(n - 2)

    fibl = {}

    def fib_dp(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        if n in fibl:
            return fibl[n]
        fibl[n] = fib_dp(n - 1) + fib_dp(n - 2)
        return fibl[n]
    num = 37
    print("Test non dp version: ")
    delt = time.time()
    a = fib(num)
    print("fib for " + str(num) + " is " + str(a))
    print("time: " + str(round((time.time() - delt) * 1000, 2)) + " ms.")

    print("Test dp version: ")
    delt = time.time()
    b = fib(num)
    print("fib for " + str(num) + " is " + str(b))
    print("time: " + str(round((time.time() - delt) * 1000, 2)) + " ms.")


def test_step(num=10):
    cache = {}

    def ways_step(n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n in cache:
            return cache[n]
        one_below = ways_step(n-1)
        two_below = ways_step(n-2)
        three_below = ways_step(n-3)
        cache[n] = one_below + two_below + three_below
        return cache[n]
    print("a " + str(num) + " steps has " + str(ways_step(num)) + " ways to go.")


test_step(4)
