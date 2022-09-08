def find_gcd(a, b):
    # r = a % b
    # while r != 0:
    #     a = b
    #     b = r
    #     r = a % b
    # return b

    while b != 0:
        temp = a
        a = b
        b = temp % b

    return a


print(find_gcd(20, 8))


