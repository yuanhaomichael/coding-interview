class Solution:
    def repeatLimitedString(self, s: str, r: int) -> str:
        # keep a frequency counter
        dic = {}
        for c in s:
            if c in dic:
                dic[c]+=1
            else:
                dic[c]=1
        
        # sort helper array from Z to A
        arr = []
        for c in dic:
            arr.append(c)
        arr.sort(reverse=True)
        
        res = ""
        cnt = 0
        
        # for each char slot, evaluate from z to a which is suitable to add, keep a cnt to check repeatlimit
        for i in range(len(s)):
            # loop thru z to a
            for j in range(len(arr)):
                ch = arr[j]
                # no more char
                if dic[ch] == 0: continue
                    
                # if res is empty or the last char is different...
                if len(res) == 0 or res[-1] != ch:
                    # add the char to the res
                    dic[ch] -= 1
                    cnt = 1  # initialize cnt
                    res += ch
                    break
                
                # if still hasn't reached the char limit 
                elif cnt + 1 <= r:
                    dic[ch] -= 1
                    cnt += 1
                    res += ch
                    break
    
        return res
            
            
            
            
            
            
            
       