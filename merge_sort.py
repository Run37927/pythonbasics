def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_array = array[:middle]
        right_array = array[middle:]

        merge_sort(left_array)
        merge_sort(right_array)

        left_pointer = 0
        right_pointer = 0
        merged_pointer = 0

        while left_pointer < len(left_array) and right_pointer < len(right_array):
            if left_array[left_pointer] < right_array[right_pointer]:
                array[merged_pointer] = left_array[left_pointer]
                left_pointer += 1
            else:
                array[merged_pointer] = right_array[right_pointer]
                right_pointer += 1
            merged_pointer += 1

        # at this point if left array still has values, add them
        while left_pointer < len(left_array):
            array[merged_pointer] = left_array[left_pointer]
            left_pointer += 1
            merged_pointer += 1

        # at this point if right array still has values, add them
        while right_pointer < len(right_array):
            array[merged_pointer] = right_array[right_pointer]
            right_pointer += 1
            merged_pointer += 1


sample = [6, 20, 8, 45, 16, 33, 78, 20]
print(sample)
merge_sort(sample)
print(sample)

