'''
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [1, 6, -1, 10] - is subsequence of array, numbers in same order, but not neccessarily adjacent in 'array'
  True
'''

# time O(n) where n is length of array
# space O(1)
def isValidSubsequence(array, sequence):
    # Write your code here.
    current_array_index = -1
    total_subs = len(sequence)
    for el in sequence:
        for i in range(current_array_index+1, len(array)):
            if el is not array[i]:
                continue
            else:
                current_array_index = i
                total_subs -= 1
    if total_subs <= 0:
        return True
    return False

# ----------------------------------------------------------------------------------------------------------------------

# time O(n) where n is length of array
# space O(1)
def isValidSubsequence(array, sequence):
    # Write your code here.
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)


