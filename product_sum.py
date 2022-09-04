def product_sum(array, multiplier=1):
    ans = 0
    for item in array:
        if type(item) is list:
            ans += product_sum(item, multiplier + 1)
        else:
            ans += item
    return ans * multiplier


a_list = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(product_sum(a_list))
