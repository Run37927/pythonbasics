test_list = [2, 4, 66, 88, 45, 32, 9, 0]


def find_max(items):
    if len(items) == 1:
        return items[0]

    op1 = items[0]
    op2 = find_max(items[1:])
    if op1 > op2:
        return op1
    else:
        return op2


print(find_max(test_list))