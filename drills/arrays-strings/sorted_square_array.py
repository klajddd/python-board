# given a sorted input array, create a sorted output array with increasing vals (negative numbers can occur)
# array": [1, 2, 3, 5, 6, 8, 9] -> [1, 4, 9, 25, 36, 64, 81]

# time O(nlog(n))
# space O(n)
def sortedSquaredArray_optimal(array):
    # Write your code here.
    result = [0] * (len(array))
    frontP = 0
    endP = len(array) - 1
    for i in range(len(array)-1, -1, -1):
        frontVal = array[frontP]
        endVal= array[endP]
        current = None
        if abs(frontVal) > abs(endVal):
            current = frontVal**2
            frontP += 1
        else:
            current = endVal**2
            endP -= 1
        result[i] = current
    return result


# ----------------------------------------------------------------------------------------------------------------------


# time O(nlog(n))
# space O(n)
def sortedSquaredArray(array):
    # Write your code here.
    result = []
    for el in array:
        result.append(el**2)
    result.sort()
    return result