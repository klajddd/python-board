from collections import defaultdict

class Solution:
    
    # time O(n log(n)) where n is length of paragraph
    # space O(n+m) where m is length of banned
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cleanParagraph = ''.join(c.lower() if c.isalpha() else " " for c in paragraph)
        words = cleanParagraph.split()
        counter = defaultdict(int)
        for word in words:
            counter[word] += 1
        sortedItems = sorted(counter.items(), key=lambda x:x[1], reverse=True)
        setBanned = set(banned)
        for item in sortedItems:
            if item[0] not in setBanned:
                return item[0]
        return None
