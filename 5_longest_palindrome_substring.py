class Solution:
    def longestPalindrome(self, s: str) -> str:
        # IDEA: for every single char or two-char, expand to the longest palindrome string. Constantly update ans.
        # TIME: O(n)
        # SPACE: O(1)

        # given a string, l and r pointers, expand to the longest palindrome substring. 
        def helper(s,l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        ans = ''
        for i in range(len(s)):
            # expand from a single char
            temp = helper(s,i,i)
            if len(temp) > len(ans):
                ans = temp
            
            # expand from a char pair
            temp = helper(s,i,i+1)
            if len(temp) > len(ans):
                ans = temp
        
        return ans
            