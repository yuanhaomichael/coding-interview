class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # IDEA: keep track of lastGoodIndex, which is where we know for sure we can get to. If current index + max jump range
        # >= lastGoodIndex, we know for sure we can get to lastGoodIndex, so we can update lastGoodIndex to the current index.
        # By the end, if lastGoodIndex is 0 we know we can get to the end from index 0. 

        # TIME: O(n)
        # SPACE: O(1)
        # https://www.youtube.com/watch?v=Zb4eRjuPHbM
        
        lastGoodIndex = i = len(nums)-1
        while i >= 0:
            if i+nums[i] >= lastGoodIndex:
                lastGoodIndex = i
            i-=1
            
        return lastGoodIndex==0