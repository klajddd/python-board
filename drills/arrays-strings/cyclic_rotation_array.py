def solution(A, K):
    # write your code in Python 3.6

    if len(A) == 0:
        return []

    K = K % len(A)

    if K == 0:
        return A

    return A[-K:] + A[:len(A) - K]


import unittest

class TestSolution(unittest.TestCase):
    def testSolution(self):
        arr = []
        k = 9
        self.assertEqual(solution(arr, k), [], 'test failed')

if __name__=="__main__":
    unittest.main()