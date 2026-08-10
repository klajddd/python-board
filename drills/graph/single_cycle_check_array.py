
'''
    jump through array by hops in each i, check if makes a cycle, i.e. visits each elem once before going
    back to the first
    '''


# time O(n)
# space O(1)
def hasSingleCycle(array):
    # Write your code here.

    elementsVisited = 0

    start = 0

    currentIdx = 0 # check every iteration if i is equal to current i, i.e. check if revisit first/same i

    n = len(array)

    while elementsVisited < n:

        if elementsVisited > 0 and currentIdx == start:
            return False

        elementsVisited += 1
        jump = array[currentIdx]
        nextIdx = (currentIdx + jump) % n
        currentIdx = None
        if nextIdx >= 0:
            currentIdx = nextIdx
        else:
            currentIdx = nextIdx + n

    return currentIdx == start



# ===================== beautifully written ============================================================================

def hasSingleCycle(array):
    # Write your code here.

    elementsVisited = 0

    currentIdx = 0

    while elementsVisited < len(array):
        if elementsVisited > 0 and currentIdx == 0:
            return False
        elementsVisited += 1
        jump = array[currentIdx]
        nextIdx = (currentIdx + jump) % len(array)
        currentIdx = nextIdx if nextIdx >= 0 else nextIdx + len(array)

    return currentIdx == 0


# ============== even more beautifully written =========================================================================

def hasSingleCycle(array):
    # Write your code here.

    elementsVisited = 0

    currentIdx = 0

    while elementsVisited < len(array):
        if elementsVisited > 0 and currentIdx == 0:
            return False
        elementsVisited += 1
        currentIdx = getNextIdx(currentIdx, array)

    return currentIdx == 0


def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)

'''
    jump through array by hops in each i, check if makes a cycle, i.e. visits each elem once before going
    back to the first

    "array": [2, 3, 1, -4, -4, 2] True
'''