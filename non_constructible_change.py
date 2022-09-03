def minchange(coins):
    change = 0
    coins.sort()
    for value in coins:
        if change + 1 < value:
            return change + 1
        change += value
    return change + 1


a_list = [5, 7, 1, 1, 2, 3, 22]
print(minchange(a_list))
