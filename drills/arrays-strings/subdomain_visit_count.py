import collections

class Solution:

    # time O(n)
    # space O(n)
    def subdomainVisits(self, cpdomains):
        count = collections.Counter()

        for cd in cpdomains:
            number, s = cd.split()
            count[s] += int(number)

            for i in range(len(s)):
                if s[i] == '.':
                    count[s[i + 1:]] += int(number)

        return [(str(count[k]) + " " + str(k)) for k in count]



import unittest


class TestSum(unittest.TestCase):

    def test_subdomainVisits(self):
        s = Solution()
        self.assertEqual(s.subdomainVisits(["9001 discuss.leetcode.com"]),
                         ['9001 discuss.leetcode.com', '9001 leetcode.com', '9001 com'], "Should be...")


if __name__ == '__main__':
    unittest.main()

# assert(1==1)

# 811. Subdomain Visit Count