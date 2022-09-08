def find_firstnonrepeatingchar(string):
    for i in range(len(string)):
        found_duplicate = False
        for j in range(len(string)):
            if string[i] == string[j] and i != j:
                found_duplicate = True
        if not found_duplicate:
            return i
    return -1
