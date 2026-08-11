class Solution:

    # time: O(u + r) where u is length of list of updates, r is length of list or result
    # space O(length)

    # def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
    def getModifiedArray(self, length: int, updates):

        result = [0] * length

        for update in updates:
            start = update[0]
            end = update[1]
            inc = update[2]

            result[start] += inc

            if end + 1 <= len(result) - 1:
                result[end + 1] += (-1) * inc
        total = 0
        for i in range(len(result)):
            total += result[i]
            result[i] = total
        return result

'''
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inc_i].

You have an array x of length length with all zeros, 
and you have some operation to apply on x. 
You should increment all the elements x[startIdxi], x[startIdxi + 1], ..., x[endIdxi] by inci.

Return x after applying all the updates.


Your input
5
[[1,3,2],[2,4,3],[0,2,-2]]

Output
[-2,0,3,5,3]
'''