class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
#       time O(T), space O(1), where T is len(T)
        
        if len(s) == 0:
            return True 
        
        if len(s) > len(t):
            return False
        
        s_ix = 0
        t_ix = 0
        
        while t_ix < len(t) and s_ix < len(s):
            if t[t_ix] == s[s_ix]:
                s_ix += 1
            t_ix += 1
            
        if s_ix == len(s):
            return True
        
        return False

s = "abc"
t = "abcde"

sol = Solution()

print(sol.isSubsequence(s, t))
                
        
            
            
                
