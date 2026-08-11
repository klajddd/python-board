# time O(n logn)
# space O(n)
def mergeOverlappingIntervals(intervals):

    if len(intervals) < 2:
        return intervals

    # intervals.sort(value=lambda x:x[0])
    sortedIntervals = sorted(intervals, key=lambda x:x[0])

    result = []

    for i in range(len(sortedIntervals)-1):

        if sortedIntervals[i][1] >= sortedIntervals[i+1][0]:
            sortedIntervals[i+1][0] = sortedIntervals[i][0]
            sortedIntervals[i+1][1] = max(sortedIntervals[i][1], sortedIntervals[i+1][1])
        else:
            result.append(sortedIntervals[i])
        if i == len(sortedIntervals) -2:
            result.append(sortedIntervals[i+1])
    return result