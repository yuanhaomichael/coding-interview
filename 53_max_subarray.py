class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # IDEA: dynamic programming, traverse each item and keep max_sum and also current_sum. The current_sum
        # help us accumulate subarray and keep track of its sum. If current_sum
        # is negative, it would not contribute to the max_sum, so we can just set it to 0, abandon it, and start a new subarray
        # in the next iteration. However, we compare max_sum and current_sum first and set the greater number to max_sum
        # because it's possible a subarray with negative sum is the max_sum. 
        
        # TIME: O(n)
        # SPACE: O(1)
        max1 = -math.inf
        sum1 = 0 
        for i in range(len(nums)):
            sum1+=nums[i]
            max1 = max(sum1, max1)
            
            if sum1<0:
                sum1 = 0
        
        return max1