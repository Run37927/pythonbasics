# def bubble(array):
#     is_sorted = False
#     while not is_sorted:
#         is_sorted = True
#         for i in range(len(array) - 1):
#             if array[i] > array[i + 1]:
#                 swap(i, i + 1, array)
#                 is_sorted = False
#     return array
#
#
# def swap(n, k, the_array):
#     temp = the_array[n]
#     the_array[n] = the_array[k]
#     the_array[k] = temp


def bubble(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


a_list = [8, 5, 2, 9, 5, 6, 3]
print(bubble(a_list))
