def find_gcd(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b



print(find_gcd(20, 8))


