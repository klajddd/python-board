from collections import defaultdict
import heapq

class Solution:
    
    # time O(n)
    # space O(n)
    def topKFrequentEfficient(self, nums, k):

        n = len(nums)

        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        helperList = [[] for _ in range(n+1)]

        for key, val in d.items():
            helperList[val].append(key)
        
        result = [] 
        for i in range(n, 0, -1):
            for el in helperList[i]:
                result.append(el)
                if len(result) == k:
                    return result
        return None

    
    # time O(n log(k))
    # space O(n)
    def topKFrequent(self, nums, k):
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        heap = []

        for key, val in d.items():
            if len(heap) < k or val > heap[0][0]:
                heapq.heappush(heap, [val, key]) # this is log k when inserting, given you are inserting at most k items
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [i[1] for i in heap]
    
    
    
    
    
    
    
import unittest

class TestSolution(unittest.TestCase):
    
    def setUp(self):
        
        self.solution = Solution()
        
        self.firstScenario = ([1,1,1,2,2,3], 2) # output: [1,2]
        self.secondScenario = ([1], 1) # output: [1]
        
    def testFirstInput(self):
        """Test a valid input."""
        print('running')
        result = self.solution.topKFrequent([1,1,1,2,2,3], 2)
        self.assertEqual(result, [2, 1], "Must be [1, 2].")
        
    def testFirstInputEfficient(self):
        """Test a valid input."""
        print('running')
        result = self.solution.topKFrequentEfficient([1,1,1,2,2,3], 2)
        self.assertEqual(result, [1, 2], "Must be [1, 2].")
        
if __name__ == "__main__":
    unittest.main()
        
    