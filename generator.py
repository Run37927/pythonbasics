a_list = [1, 2, 3, 4, 5, 6]


def geni():
    for num in range(15):
        yield num**num

geni()
