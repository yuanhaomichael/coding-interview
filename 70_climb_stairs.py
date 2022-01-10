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