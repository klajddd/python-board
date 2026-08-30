class Solution:

    '''
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    '''


    #     time: O(n) --> n = number of intervals
    #     space: O(1)
    def merge(self, intervals):

        # sort
        intervals = sorted(intervals, key=lambda item: item[0])

        i = 0

        while i <= len(intervals) - 2 and len(intervals) > 1:

            first = intervals[i]

            second = intervals[i + 1]

            if first[1] >= second[0]:
                if first[1] > second[1]:
                    intervals[i: i + 2] = [intervals[i]]
                else:
                    intervals[i: i + 2] = [[intervals[i][0], intervals[i + 1][1]]]

            else:
                i += 1

        return intervals


s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
