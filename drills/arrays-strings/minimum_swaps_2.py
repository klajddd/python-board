
class Solution:
    def minimumSwaps(self, arr):

        if arr is None:
            return None

        length = len(arr)

        i = 0
        swaps = 0

        while i < length:
            if arr[i] != (i + 1):
                temp1 = arr[i]
                temp2 = arr[arr[i] - 1]
                arr[arr[i] - 1] = temp1
                arr[i] = temp2
                swaps += 1
            else:
                i += 1

        print(f"arr is {arr}")
        return swaps


import unittest

class TestSolution(unittest.TestCase):
    s = Solution()

    def test_populated_array(self):

        array = [2, 3, 4, 1, 5]
        self.assertEqual(3, self.s.minimumSwaps(array), "Should be 3")

    def test_empty_array(self):
        array = []
        self.assertEqual(0, self.s.minimumSwaps(array), "Should be 0")

    def test_none(self):
        self.assertEqual(None, self.s.minimumSwaps(None), 'should be none')


if __name__ == '__main__':
    unittest.main()