class Solution(object):

# time: O (n+m)(log m)
# space: O(n) (I think, or O(1))
    def successfulPairs(self, spells, potions, success):
        
        n = len(spells)
        m = len(potions)
        pairs = [None] * n
        potions.sort()

        for i in range(n):
            spell = spells[i]
            left = 0
            right = m - 1
            
            # perform binary search
            while left <= right:
                mid = left + (right - left) // 2
                product = spell * potions[mid]
                if product >= success:
                    right = mid - 1
                else:
                    left = left + 1
            pairs[i] = m - left
        return pairs

        
        return result
