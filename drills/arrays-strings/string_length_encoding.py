'''
AAAAAAAAAAAAABBCCCCDD -> 9A4A2B4C2D

'''

# time O(n)
# space O(n)

def runLengthEncoding(string):
    # Write your code here.
    result = []
    count = 1

    for i in range(1, len(string)):
        current = string[i]
        prev = string[i-1]

        if current != prev or count ==9:
            result.append(str(count)+prev)
            count = 0
        count += 1

    result.append(str(count)+string[-1])
    return "".join(result)

# ----------------------------------------------------------------------------------------------------------------------
import unittest

class TestProblem(unittest.TestCase):
    def test_runLengthEncoding(self):
        self.assertEqual(runLengthEncoding('AAAAAAAAAAAAABBCCCCDD'), '9A4A2B4C2D')

if __name__=="__main__":
    unittest.main()

# ----------------------------------------------------------------------------------------------------------------------

# assert(runLengthEncoding('AAAAAAAAAAAAABBCCCCDD')=='9A4A2B4C2D')