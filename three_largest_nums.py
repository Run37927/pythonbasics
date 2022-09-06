def findThreeLargestNumbers(array):
    # Write your code here.
    res = [None, None, None]
    for num in array:
        update_largest(res, num)
    return res

def update_largest(res, num):
    if res[2] is None or num > res[2]:
        shift_and_update(res, num, 2)
    elif res[1] is None or num > res[1]:
        shift_and_update(res, num, 1)
    elif res[0] is None or num > res[0]:
        shift_and_update(res, num, 0)

def shift_and_update(array, num, idx):
    for i in range(idx+1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]


sample = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(sample))
