# avg case time: nlogn, space: log(n)
def quick(array):
    quick_helper(array, 0, len(array) - 1)
    return array


def quick_helper(array, start, end):
    if start >= end:
        return
    pivot_index = start
    left_index = start + 1
    right_index = end

    while right_index >= left_index: # while they haven't crossed each other
        if array[left_index] > array[pivot_index] > array[right_index]:
            swap(left_index, right_index, array)
        if array[left_index] <= array[pivot_index]:
            left_index += 1
        if array[right_index] >= array[pivot_index]:
            right_index -= 1

    # now left right have crossed, so swap value at pivot and value at right pointer
    swap(pivot_index, right_index, array)

    left_subarr_is_smaller = right_index - 1 - start < end - (right_index + 1)
    if left_subarr_is_smaller:
        quick_helper(array, start, right_index - 1)
        quick_helper(array, right_index + 1, end)
    else:
        quick_helper(array, right_index + 1, end)
        quick_helper(array, start, right_index - 1)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
