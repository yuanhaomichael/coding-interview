class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # IDEA: keep track of the lowest buy day and the largestDiff
        # if we meet a lower buy day, we update the buyTime
        # return the largestDiff at the end
        
        # TIME: O(n)
        # SPACE: O(1)
        
        buyTime = 0
        largestDiff = 0
        for i in range(len(prices)):
            if prices[i]<prices[buyTime]:
                buyTime = i
            
            largestDiff = max(largestDiff, prices[i]-prices[buyTime])
        
        return largestDiff
            
            
        
            