class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # IDEA: dynamic programming, traverse each item and keep max_sum and also current_sum. The current_sum
        # help us accumulate subarray and keep track of its sum. If current_sum
        # is negative, it would not contribute to the max_sum, so we can just set it to 0, abandon it, and start a new subarray
        # in the next iteration. However, we compare max_sum and current_sum first and set the greater number to max_sum
        # because it's possible a subarray with negative sum is the max_sum. 

        #  Any negative sum would only decrease the sum of any subsequent subarray. 
        #  Therefore, if sum1 becomes negative, it implies that including the elements 
        #  seen so far would only reduce the overall sum of any future subarray.
        
        # TIME: O(n)
        # SPACE: O(1)
        max1 = -math.inf
        sum1 = 0 
        [-1, 2, -5, 3]
        for i in range(len(nums)):
            sum1+=nums[i]
            max1 = max(sum1, max1)
            
            if sum1<0:
                sum1 = 0
        
        return max1
    
# solution 2
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # IDEA: compute cumulative sum and store in an array.
        # find the max gap between 2 numbers in this cumulative sum array, which will be the max sub array sum.
        # 
        # To find the max gap between 2 numbers in an array, while having minIdx < maxIdx, 
        # 1. set the minValue as the first value, iterate from 1 to end
        # 2. for each iteration, update maxGap if gap is larger
        #       then update minValue if current element is smaller

        curSum = 0
        rs = []
        for i in range(len(nums)):
            curSum += nums[i]
            rs.append(curSum)
        
        rs = [0] + rs
        
        if len(nums) == 1: 
            return nums[0]

        minValue = rs[0]
        maxDiff = rs[1] - rs[0]
        for i in range(1, len(rs)):
            if rs[i] - minValue > maxDiff:
                maxDiff = rs[i] - minValue

            if rs[i] < minValue:
                minValue = rs[i]
            

        return maxDiff                


                



        

            

