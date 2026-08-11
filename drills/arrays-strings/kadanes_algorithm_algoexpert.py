# write a function that takes in a non-empty array of integers and return the max sum that can be
# obtained by adding all integers in a non-empty subarray of the input array
# the subarray must contain only adjecent numbers



# time O(n)
# sapce O(1)
def kadanesAlgorithm(array):
    # Write your code here.
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        num = array[i]
        maxEndingHere = max(num, (maxEndingHere + num))
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar
