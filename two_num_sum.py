def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array) -1):
        first_num = array[i]
        for j in range(i+1, len(array)):
            second_num = array[j]
            if first_num + second_num == targetSum:
                return [first_num, second_num]
    return []


def main():
    a_list = [3, 5, -4, 8, 11, 1, -1, 6]
    print(twoNumberSum(a_list, 10))


if __name__ == '__main__':
    main()
