# time O(n)
# space O(1)
def firstDuplicateValue_optimal(array):
    for value in array:

        absValue = abs(value)

        if array[absValue-1] < 0:
            return absValue

        array[absValue-1] *= -1
    return -1

# ----------------------------------------------------------------------------------------------------------------------

# time O(n)
# space O(n)
def firstDuplicateValue(array):
    # Write your code here.
    sett = set()
    for el in array:
        if el in sett:
            return el
        else:
            sett.add(el)
    return -1


array = [2, 1, 5, 2, 3, 3, 4]
assert firstDuplicateValue_optimal(array) == 2