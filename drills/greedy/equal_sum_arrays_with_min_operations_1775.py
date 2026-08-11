class Solution:
    
    # time: O((N + M) * log(N + M)).
    # space: O(N+M)
    
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        
        d = abs(sum1 - sum2)
        
        tempList = []
        
        if sum1 < sum2:
            tempList += [6-e for e in nums1]
            tempList += [e-1 for e in nums2]
        else:
            tempList += [6-e for e in nums2]
            tempList += [e-1 for e in nums1]
        
        tempList.sort(reverse=True)
        result = 0
        while d > 0 and result < len(tempList):
            d-=tempList[result]
            result += 1
        return result if d <= 0 else -1






        if sum1 > sum2:
            return self.minOperations(nums2, nums1)
        ans = 0
        count = [None] * 6
        

        return ans
