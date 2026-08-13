class Solution:
    def shortestDistance(self, words: list[str], word1: str, word2: str) -> int:
        
        distance = float('inf')
        
        word1_previous = -1
        
        word2_previous = -1
        
        for i in range(len(words)):
            
            if words[i] == word1:
                
                word1_previous = i
                
            elif words[i] == word2:
                
                word2_previous = i
                
            if word1_previous > -1 and word2_previous > -1:
                
                distance = min(distance, abs(word1_previous - word2_previous))
                
        return distance