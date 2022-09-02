def is_valid_subsequence(array, sequence):
    arr_index = 0
    seq_index = 0
    while arr_index < len(array) and seq_index < len(sequence):
        if array[arr_index] == sequence[seq_index]:
            seq_index += 1
        arr_index += 1
    return seq_index == len(sequence)
