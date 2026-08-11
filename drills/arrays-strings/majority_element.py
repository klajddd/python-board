class Solution:

    # O(n) time
    # O(1) space
    def efficient_majorityElement(self, nums) -> int:

        counter = 0

        el = None

        for num in nums:
            if counter == 0:
                el = num
                counter = 1
            else:
                if el == num:
                    counter += 1
                else:
                    counter -= 1
                    if counter == 0:
                        el = None
        return el


    def majorityElement(self, nums) -> int:

        length = len(nums)

        majority = length / 2

        occurrences = {}

        for num in nums:
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1

        for k, v in occurrences.items():
            if v > majority:
                return k

    # def is_target_the_majority_element_in_sorted_array(self):


    def majority_Element_ii_find_all(self, nums):

        majority = len(nums) / 3

        occ = {}

        result = []

        for num in nums:
            if num in occ:
                occ[num] += 1
            else:
                occ[num] = 1

        for k, v in occ.items():
            if v > majority:
                result.append(k)

        return result


import unittest

class TestSolution(unittest.TestCase):

    s = Solution()
    nums1 = [3, 2, 3, 3, 1]

    def test_majority(self):
        self.assertEqual(self.s.majorityElement(self.nums1), 3, 'should be 3')

    def test_majority_efficient(self):
        self.assertEqual(self.s.majorityElement(self.nums1), 3, 'should be 3 efficient')

if __name__ == '__main__':
    unittest.main()

