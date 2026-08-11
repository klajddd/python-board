# time O(n)
# space O(1)
def findThreeLargestNumbers(array):
    # Write your code here.
    largest = float('-inf')
    s_largest = float('-inf')
    t_largest = float('-inf')

    for el in array:
        if el > largest:
            t_largest = s_largest
            s_largest = largest
            largest = el
        elif el > s_largest:
            t_largest = s_largest
            s_largest = el
        elif el > t_largest:
            t_largest = el

    return [t_largest, s_largest, largest]


'''
input:
"array": [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

result:
[18, 141, 541]
'''