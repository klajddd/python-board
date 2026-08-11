def maxSubsetSumNoAdjacent(array):
    # Write your code here.

    # [75, 105, 120, 75, 90, 135]
    n = len(array)

    max_sums = [0] * n

    max_sums[0] = array[0]

    max_sums[1] = max(array[0], array[1])

    for i in range(2, n):
        max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])

    return max_sums[-1]

print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))