'''
input: ['cat', 'dog', 'god']
output: [{'cat'}, {'dog', 'god'}]
'''




# time O(n * w)
# space O(wn + 26n) ---> O(wn)  ----> n is list of words, w is longest word
class Solution:
    
    def groupAnagramsEfficient(self, strs):
        
        from collections import defaultdict
        
        anagramsMap = defaultdict(list)
        
        for word in strs:
            counter = [0] * 26
            for letter in word:
                counter[ord('letter') - ord('a')] += 1
                
            anagramsMap[tuple(counter)].append(word)

        return list(anagramsMap.values())

# time O(n * w*log(w))
# space O(wn) - n is list of words, w is longest word
class Solution:
    
    def groupAnagramsEfficient(self, strs):
        
        from collections import defaultdict
        
        anagramsMap = defaultdict(list)
        
        for el in strs:
            sortedEl = ''.join(sorted(el))
            anagramsMap[sortedEl].append(el)

        return list(anagramsMap.values())
    
    
    
    
    def groupAnagrams(self, anagrams):
        output = {}
        for a in anagrams:
            if ''.join(sorted(a)) in list(output.keys()):
                # append
                output[''.join(sorted(a))].add(a)
            else:
                output[''.join(sorted(a))] = {a}
        return list(output.values())


anagrams = ['cat', 'dog', 'god']
s = Solution()
print(s.groupAnagrams(anagrams))
assert s.groupAnagrams(anagrams) == [{'cat'}, {'dog', 'god'}]
