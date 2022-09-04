def minimumWaitingTime(queries):
    # Write your code here.
    if len(queries) == 1:
        return 0
    queries.sort() # built in sort nlogn
    # res = []
    # t = 0
    # for i in range(len(queries) - 1):
    #     t += queries[i]
    #     res.append(t)
    # return sum(res)

    min_time = 0
    for i in range(len(queries)):
        min_time += queries[i] * (len(queries) - (i + 1))
    return min_time



q = [3, 2, 1, 2, 6]
print(minimumWaitingTime(q))
