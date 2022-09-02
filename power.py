def power(num, pow):
    if pow == 0:
        return 1
    else:
        return num * power(num, pow - 1)


print(power(5, 3))