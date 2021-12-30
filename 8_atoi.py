# IDEA: Follow the steps to process the string, check if it's a number 
# by using ord() to see if it's in [48, 57] (ASCII for 0-9)

#TIME: O(n)
#SPACE: O(1)
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        
        # process the sign
        sign = 0
        if(s!=''):
            if s[0]=='+':
                sign = 1
                s = s[1:]
            elif s[0] == '-':
                sign = -1
                s = s[1:]
            # if the char is not a number nor a sign
            elif ord(s[0]) < 48 or ord(s[0]) > 57:
                return 0
            else: 
                sign = 1
        else: 
            return 0
            
        # get rid of the rest of the string
        for i in range(len(s)):
            if s[i] == ' ':
                s = s[:i]
                break
            elif ord(s[i]) < 48 or ord(s[i]) > 57:
                s = s[:i]
                break
        
        multiplier = len(s) - 1
        integer = 0
        # convert to integer, eg. '00033' -> 33
        for i in range(len(s)):
            integer += int(s[i]) * (10**multiplier)
            multiplier-=1
            
        # clamping the integer
        if -(2**31) <= integer*sign <= (2**31)-1:       
            return integer*sign
        else:
            if integer*sign < -2**31:
                return -2**31
            elif integer*sign > 2**31-1:
                return 2**31-1
            
    

                
                
            
                