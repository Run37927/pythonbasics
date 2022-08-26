def add_numbers(*args): # args always come back as tuple
    total = 0
    for num in args:
        total = total + num
    return total


print(add_numbers(1, 3, 5, 7, 9))
