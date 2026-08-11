'''
1351. Count Negative Numbers in a Sorted Matrix
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
    return the number of negative numbers in grid.

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
'''


class Solution:
    # O(n * log m)
    # O(1)
    def countNegatives(self, grid) -> int:
        result = 0
        for l in grid:
            negatives = self.countNegativesInList(l)
            result += negatives
        return result

    @staticmethod
    def countNegativesInList(l):
        hi = len(l) - 1
        lo = 0
        while hi >= lo:
            mid = (hi + lo) // 2
            if l[mid] >= 0:
                lo = mid + 1
            else:
                hi = mid - 1
        return len(l) - lo

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
s = Solution()

assert 8 == s.countNegatives(grid)