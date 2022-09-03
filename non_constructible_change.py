def minchange(coins):
    change = 0
    coins.sort()
    for value in coins:
        if change + 1 < value:
            return change + 1
        change += value
    return change + 1