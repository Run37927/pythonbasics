# avg case time: nlogn, space: log(n)
def quick(array):
    quick_helper(array, 0, len(array) - 1)
    return array


def quick_helper(subarr, start, end):
    if start >= end:
        return
    pivot_index = start
    left_index = start + 1
    right_index = end

    while right_index >= left_index:
        if subarr[left_index] > subarr[pivot_index] > subarr[right_index]:
            swap(left_index, right_index, subarr)
        if subarr[left_index] <= subarr[pivot_index]:
            left_index += 1
        if subarr[right_index] >= subarr[pivot_index]:
            right_index -= 1
    swap(pivot_index, right_index, subarr)
    left_subarr_is_smaller = right_index - 1 - start < end - (right_index + 1)
    if left_subarr_is_smaller:
        quick_helper(subarr, start, right_index - 1)
        quick_helper(subarr, right_index + 1, end)
    else:
        quick_helper(subarr, right_index + 1, end)
        quick_helper(subarr, start, right_index - 1)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
