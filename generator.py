def geni():
    for num in range(50):
        yield num**num


my_var_generator = geni()
all_nums = list(my_var_generator)
print(all_nums)

for big_num in my_var_generator:
    print(big_num)
