def bubble(array):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                is_sorted = False
    return array


def swap(n, k, the_array):
    temp = the_array[n]
    the_array[n] = the_array[k]
    the_array[k] = temp


a_list = [8, 5, 2, 9, 5, 6, 3]
print(bubble(a_list))
