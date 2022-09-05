# def binary_search(array, target):
#     # prerequiste: the list is already sorted
#     return helper(array, target, 0, len(array) - 1)
#
#
# def helper(array, target, left, right):
#     if left > right:
#         return -1
#     middle = (left + right) // 2
#     if array[middle] == target:
#         return middle
#     elif target < array[middle]:
#         return helper(array, target, left, middle - 1)
#     else:
#         return helper(array, target, middle + 1, right)
#

def binary_search(array, target):
    return helper(array, target, 0, len(array) - 1)


def helper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif target < array[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1