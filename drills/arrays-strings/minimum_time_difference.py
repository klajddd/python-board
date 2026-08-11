# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes
# difference between any two time-points in the list.
# Input: timePoints = ["23:59","00:00"]


class Solution:

    # time O(n), n is the number of timepoints
    # space O(1)
    def findMinDifference(self, timePoints):
        bucket = [False for _ in range(60 * 24)]

        for timePoint in timePoints:
            hours, minutes = timePoint.split(':')
            total_time = int(hours) * 60 + int(minutes)
            if bucket[total_time]:
                return 0
            bucket[total_time] = True

        minimum = float('inf')
        first = -1
        prev = -1
        curr = -1

        for i in range(len(bucket)):
            if bucket[i]:
                if prev == -1:
                    prev = i
                    first = i # won't touch again
                else:
                    curr = i
                    minimum = min(minimum, curr-prev)
                    prev = curr
        return min(minimum, 1440 - curr + first)
