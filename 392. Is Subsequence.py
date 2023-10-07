class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) <= 0:
            return True
        
        a, b = 0, 0
        while b < len(t):
            if s[a] == t[b]:
                a += 1
                b += 1
                if a >= len(s):
                    return True
            else:
                b += 1
        
        return False
    

# End sat 7 oct 2023