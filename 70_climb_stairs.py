class Solution:
    def climbStairs(self, n: int) -> int:
        # IDEA: going backwards, second holds the ways to get to the latter stairs,
        # first holds the ways to get to the former stairs. first+second gives the ways
        # to get to the stairs before both stairs.
        
        # TIME: O(n)
        # SPACE: O(1)        
        first = second = 1
        for i in range(n-1): # going backwards
            temp = first
            first = first+second
            second = temp
        
        return first


# Approach 2: DP

class Solution:
    def climbStairs(self, n: int) -> int:
        # base case
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        pp = 1
        p = 2
        
        # inductive rule
        # At any given level,
        # assuming that I know the answer to level-1 and level-2
        # res[level] = res[level-1] + res[level-2]
        for i in range(2, n):
            cur = pp + p
            pp = p
            p = cur
            
            
        return p
        
        