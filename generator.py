a_list = [1, 2, 3, 4, 5, 6]


def geni():
    for num in range(50):
        yield num**num

for big_num in geni():
    print(big_num)
