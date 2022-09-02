def is_valid_subsequence(array, sequence):
    # arr_index = 0
    # seq_index = 0
    # while arr_index < len(array) and seq_index < len(sequence):
    #     if array[arr_index] == sequence[seq_index]:
    #         seq_index += 1
    #     arr_index += 1
    # return seq_index == len(sequence)



    seq_index = 0
    for num in array:
        if seq_index == len(sequence):
            break
        if sequence[seq_index] == num:
            seq_index += 1
    return seq_index ==  len(sequence)