# cache = {}
# def get_nth_fib(n):
#     # using memoization
#     global cache
#     if n in cache:
#         return cache[n]
#
#     if n == 0:
#         result = 0
#     elif n == 1:
#         result = 1
#     else:
#         result = get_nth_fib(n-1) + get_nth_fib(n-2)
#     cache[n] = result
#     return result


def get_nth_fib(n):
    # iterative approach
    last_two = [0,1]
    counter = 3
    while counter <= 3:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[1] if n > 1 else 0