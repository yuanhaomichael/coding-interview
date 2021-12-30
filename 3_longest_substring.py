class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #IDEA: a sliding window that keeps track of the largest unique substring. If there is a duplicate discovered
        #on the right, increment left until we exclude that character. Use a set to keep track of duplicates.
        
        #TIME: O(n), the pointers always move right, and one iteration through the entire string
        #SPACE: Using a set of unique chars from the string, O(n)
        
        l = 0;
        charSet = set()
        res = 0
        for r in range(len(s)):
            if s[r] in charSet:
                # increment left to exclude this character
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l+=1
                l+=1
            else: 
                # add char to charSet
                charSet.add(s[r])
            
            res = max(res, r-l+1)
            
            
        return res