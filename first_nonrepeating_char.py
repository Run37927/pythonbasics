# def find_firstnonrepeatingchar(string):
#     for i in range(len(string)):
#         found_duplicate = False
#         for j in range(len(string)):
#             if string[i] == string[j] and i != j:
#                 found_duplicate = True
#         if not found_duplicate:
#             return i
#     return -1


def find(string):
    # using dictionary
    counts = {} #space is constant
    for char in string:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

    for char in string:
        if counts[char] == 1:
            return string.index(char)
