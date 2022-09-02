# [5, 11, 3, 50, 60, 90] with k = 2 where k is the number of transactions we can make

# def maxProfitWithKtransaction(prices, k):
#     if len(prices) == 0:
#         return 0
#     profits = [[0 for day in prices] for transac in range(k + 1)]
#     for transac in range(1, k+1):
#         maxThusFar = float("-inf")
#         for day in range(1, len(prices)):
#             maxThusFar = max(maxThusFar, profits[transac-1][day-1] - prices[day-1])
#             profits[transac][day] = max(profits[transac][day-1], maxThusFar + prices[day])
#
#     return profits[-1][-1]

# O(nk) time
# O(nk) space

def maxProfitWithKtransaction(prices, k):
    if len(prices) == 0:
        return 0
    even_profits = [0 for day in prices]
    odd_profits = [0 for day in prices]
    for transac in range(1, k+1):
        max_thus_far = float("-inf")
        if transac % 2==1:
            current_profits = odd_profits
            previous_profits = even_profits
        else:
            current_profits = even_profits
            previous_profits = odd_profits
        for day in range(1, len(prices)):
            max_thus_far = max(max_thus_far, previous_profits[day-1] - prices[day-1])
            current_profits[day] = max(current_profits[day-1], max_thus_far + prices[day])

    return even_profits[-1] if k % 2 == 0 else odd_profits[-1]
# O(nk) time / O(n) space
