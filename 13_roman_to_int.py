class Solution:
    def romanToInt(self, s: str) -> int:
        #IDEA: add all characters together based on a dictionary that converts romans to integer
        #if there is instances of substraction (IV, IX, XL, XC, CD, CM), we substract twice the first letter's integer value
        #TIME: O(n)
        #SPACE: O(1)
        
        r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
            
        # find instances of substraction
        sub = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
        i = 0
        
        # for each character, add its roman value to result
        # at the same time, get current and next chars as a pair and check if it's an instance of substraction
        # if it is, minus the integer value of the first roman char twice
        while i < len(s)-1:
            char = s[i]
            res+=r[s[i]]
            pair = s[i] + s[i+1]
            if pair in sub:
                res = res - 2*r[s[i]]
            i+=1
            
        # the loop goes through from 0-> (len(s)-2), so we need to add the integer value of the last roman numeral
        res+=r[s[len(s)-1]]
        
        return res