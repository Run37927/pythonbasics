def selection_sort(array):
    current_index = 0  # this is the first index of the current unsorted list
    while current_index < len(array) - 1:
        # when current index reach to the last index in the list, that means we are done
        smallest_index = current_index  # assign current index to smallest index
        for i in range(current_index + 1, len(array)):
            if array[smallest_index] > array[i]:
                smallest_index = i
        swap(current_index, smallest_index, array)
        current_index += 1
    return array


def swap(x, y, a_list):
    a_list[x], a_list[y] = a_list[y], a_list[x]


sample = [2, 34, 15, 7, 0, 8]
print(selection_sort(sample))

