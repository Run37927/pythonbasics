def insertion(array):
    # looping through array once
    for i in range(1, len(array)):
        j = i
        # looping backwards to do swapping in the tentatively sorted sublist
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array


def swap(k, m, a_list):
    a_list[k], a_list[m] = a_list[m], a_list[k]


sample = [8, 5, 2, 9, 5, 6, 3]
print(insertion(sample))
