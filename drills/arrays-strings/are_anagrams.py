class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMap = {}
        for char in s:
            if char in countMap:
                countMap[char] += 1
            else:
                countMap[char] = 1
        for char in t:
            if char in countMap:
                countMap[char] -= 1
            else:
                return False
        for k, v in countMap.items():
            if v != 0:
                return False
        return True

