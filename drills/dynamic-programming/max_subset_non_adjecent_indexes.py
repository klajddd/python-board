'''
dynamic programming
find max subset in array of positive numbers where numbers are not adjacent
keep track of indexes

BASE CASE:
max of 1 value is itself --- max_sums[0] = array[0]
max of 2 probabilities is the max between those 2 --- max_sums[1] = max(array[0], array[1])
'''

# O(n) time | O(n) space
def max_subset_sum_no_adjacent(array):

    if len(array) < 1:
        return 0

    if len(array) < 2:
        return array[0]

    n = len(array)

    max_sums = [0] * n

    max_sums[0] = array[0]

    max_sums[1] = max(array[0], array[1])

    for i in range(2, n):
        max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])

    return max_sums[-1]


# O(n) time | O(1) space
def max_subset_sum_no_adjacent_efficient_space(array):

    # [75, 105, 120, 75, 90, 135]
    if len(array) < 1:
        return 0
    if len(array) < 2:
        return array[0]

    n = len(array)
    max_one = array[0]
    max_two = max(array[0], array[1])

    for i in range(2, n):
        current_max = max(max_two, max_one + array[i])
        max_one = max_two
        max_two = current_max

    return max_two


print(max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135]))
print(max_subset_sum_no_adjacent_efficient_space([75, 105, 120, 75, 90, 135]))
