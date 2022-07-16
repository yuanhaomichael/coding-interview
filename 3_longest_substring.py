class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #IDEA: a sliding window that keeps track of the largest unique substring. If there is a duplicate discovered
        #on the right, increment left until we exclude that character. Use a set to keep track of duplicates.
        
        # checking duplication is simple, whenever we encounter a new char, check if it's in the set

        #TIME: O(n), the pointers always move right, and one iteration through the entire string
        #SPACE: Using a set of unique chars from the string, O(n)
        
        l = 0;
        charSet = set()
        res = 0
        for r in range(len(s)):
            if s[r] in charSet:
                # increment left pointer and removing char from char set as we go
                # until we exclude this character
                # Note that s[r] isn't added to the set and the duplicate char isn't
                # removed from the set, so the charSet is up to date with the sliding window
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l+=1
                l+=1  # going one character past the first duplicate occurence
            else: 
                # add char to charSet
                charSet.add(s[r])
            
            res = max(res, r-l+1)
            
            
        return res