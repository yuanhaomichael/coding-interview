class Solution:
    def minWindow(self, s: str, t: str) -> str:
       # IDEA: have a hashmap that keeps track of the 
       # character count in t. Use left and right pointer
       # and advance the right pointer when we are trying to
       # expand the window. 

       # As we expand the window, if s[right] is in the hashmap,
       # we decrement hashmap[s[right]]

       # when the window includes all chars in t, we update min_window and begin 
       # to increment the left pointer. If s[left] is in hashmap,
       # we increment hashmap[s[left]]

        from collections import Counter

        dic = Counter(t)

        if len(s) < len(t):
            return ""

        min_window = ""
        l = 0
        r = 0
        cnt = len(t)

        while r < len(s):
            if s[r] in dic:
                if dic[s[r]] > 0:
                    cnt -= 1
                dic[s[r]] -= 1

            while cnt == 0:
                # update min_window
                if r-l + 1 < len(min_window) or min_window == "":
                    min_window = s[l:r+1]
                # increment left pointer
                
                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] > 0:
                        cnt += 1 # cnt keeps track of how many letters in t is in the current window
                l += 1
            r+=1

        
        return min_window
            






