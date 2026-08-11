from collections import defaultdict


class Solution:

    # time O(n)
    # space O(1)

    def minSteps(self, s: str, t: str) -> int:
        lettersMap = defaultdict(int)
        for l in s:
            lettersMap[l] += 1
        
        for l in t:
            lettersMap[l] -= 1

        total = 0
        for k, v in lettersMap.items():
            total += abs(v)
        return total // 2
        