cache = {}
def get_nth_fib(n):
    # using memoization
    global cache
    if n in cache:
        return cache[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = get_nth_fib(n-1) + get_nth_fib(n-2)
    cache[n] = result
    return result
