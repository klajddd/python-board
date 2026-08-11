# time O(n log n)
# space O(1)
'''
    [1 2 2 3 6]
     0 1 3 5 8
     0 1 4 9 17
             ^
    t =8
    r =17
    write a function that returns the minimum total amount of waiting time
'''

def minimumWaitingTime(queries):
    # Write your code here.
    total = 0
    result = 0

    queries.sort()
    print(queries)

    for i in range(1, len(queries)):
        prev = queries[i - 1]
        total += prev
        result += total
        print(result)

    return result
