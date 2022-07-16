class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        #  IDEA: streak keeps track of the size of the longest inceasing subarray. 
        #  max_streak = (max_streak, streak)
        
        # TIME: O(n)
        # SPACE: O(1)
        
        streak = 1
        max_streak = 0
        
        #  traverse the array and constantly check the next element. Stop at the second to last position. [1, 3, 2]
        for i in range(len(nums)):
            if i < len(nums)-1:
                next_element = nums[i+1]
                # if strictly increasing
                if next_element > nums[i]:
                    streak+=1
                    continue
                else: 
                    # when the ascending subarray ends
                    max_streak = max(max_streak, streak)
                    streak = 1
            else:
                max_streak = max(max_streak, streak)
                
        return max_streak
                
            
            