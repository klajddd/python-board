'''
array": [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        result =        [                 ] -> length = 6
'''

# time O(n)
# space O(1)
def longestPeak(array):
    # Write your code here.
    longestPeakLength = 0
    i = 1
    while i<len(array)-1:
        isPeak = array[i-1] < array[i] and array[i] > array[i+1]
        if not isPeak:
            i+= 1
            continue

        leftIdx = i - 2 # expand in left direction by 2 since we know we have a peak
        while leftIdx  >= 0 and array[leftIdx] < array[leftIdx +1]:
            leftIdx -= 1

        rightIdx = i + 2 # same here
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx-1]:
            rightIdx += 1

        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIdx
    return longestPeakLength
