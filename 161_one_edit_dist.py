class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # if the two string lengths differ by over 1, return False
        if abs(len(s) - len(t)) > 1:
            return False
        
        # first case: how do we add a char in the shorter str, to get the longer str
        # two pointers: if first instance of different char, increment the pointer of the longer string
        # if the pointer points at the same char as the shorter string, we keep going.
        # else: we return False
        elif len(s) != len(t):
            if len(s) == 0 or len(t) == 0:
                return True
            shorter = longer = ""
            if len(s) > len(t):
                shorter = t
                longer = s
            else:
                shorter = s
                longer = t

            l = r = 0
            cnt = 0
            while l < len(shorter) and r < len(longer):
                if shorter[l] != longer[r] and cnt < 1:
                    cnt+=1
                    r+=1
                elif shorter[l] != longer[r] and cnt == 1:
                    return False
                else:
                    l+=1
                    r+=1
            return True
                
                
        else: 
        # second case: if 2 str are equal in length, see how many chars the two string differs. if over 1, return False
            cnt = 0
            for i in range(len(s)):
                if s[i]!=t[i]:
                    cnt+=1
    
            if cnt == 1:
                return True
            else:
                return False