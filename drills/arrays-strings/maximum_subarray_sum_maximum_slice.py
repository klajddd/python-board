# a = [5, -7, 3, 5, -2, 4, -1]


# time O(n) - linear
def maximum_subarray_sum_3(arr):
    max_ending = 0
    max_slice = 0
    for a in arr:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

# time O(n^2) - quadratic
def maximum_subarray_sum_2(arr):
    n = len(arr)
    result = float('-inf')

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            result = max(result, sum)

    return result



# time O(n^3) - cubic
def maximum_subarray_sum(arr):
    n = len(arr)
    result = float('-inf')
    for i in range(n):
        for j in range(i, n):
            total = 0
            for k in range(i, j + 1):
                total += arr[k]
            result = max(result, total)
            total = 0
    return result



def test(arr):
    max_ending = 0
    max_slice = 0
    for num in arr:
        max_ending = max(0, num + max_ending)
        max_slice = max(max_slice, max_ending)
    return max_slice

a = [5, -7, 3, 5, -2, 4, -1]

print(maximum_subarray_sum(a))
print(maximum_subarray_sum_2(a))
print(maximum_subarray_sum_3(a))
print(test(a))