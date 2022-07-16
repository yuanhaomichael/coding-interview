class Solution:
    def minSteps(self, s: str, t: str) -> int:

        from collections import Counter
        s = Counter(s)
        t = Counter(t)
        
        sum1 = 0
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            sum1 += (abs(s[ch] - t[ch]))                
            

        return sum1