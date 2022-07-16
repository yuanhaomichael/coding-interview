class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # IDEA: x XOR y reveals the different bits. If 2 bits are different, their XOR will be 1. 
        # we store the XOR result and count the number of 1s in the result. 
        # TIME: O(B), number of bits of max(x,y)
        # SPACE: O(B)
        dist = str(format(x^y, 'b'))
        arr = [int(i) for i in dist]
        res = sum(arr)
        return res

# Approach 2
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # IDEA: use built in function
        # TIME: O(1)
        # SPACE: O(1)
        return bin(x^y).count('1')

# Approach 3
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # IDEA: right shift a step at a time and check if the right most slot is 1. 
        # If it is, increment count.
        # TIME: O(1)
        # SPACE: O(1)
        xor = x ^ y
        dist = 0
        while xor:
            if xor % 2 == 1:
                dist+=1
            xor = xor>>1
        return dist

# Approach 4:
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # IDEA: when number AND number-1, the rightmost 1 bits of number will be cleared
        # TIME: O(1)
        # SPACE: O(1)
        
        xor = x ^ y
        dist = 0
        while xor:
            dist+=1
            # clear the right most 1
            xor = xor & (xor-1)
        return dist
