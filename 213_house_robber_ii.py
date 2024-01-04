class Solution:
    def rob(self, nums: List[int]) -> int:
        # IDEA: 
        # if I rob the current house, store prev prev house max amount + current house
        # if I don't rob the current house, store the prev house max amount
        # The circular nature of houses make it so that if we rob the first house, we must not 
        # rob the last house.
        # TIME: O(N)
        # SPACE: O(N)
        
        # minimal case consideration
        if(len(nums) <= 1):
            return nums[0]
            
        # initialization of memo arrays, 2 of them is given first house is not robbed,
        # 2 of them is given first house is robbed
        first_robbed_rob,first_robbed_norob,first_norobbed_rob,first_norobbed_norob = [0 for i in range(len(nums))],[0 for i in range(len(nums))],[0 for i in range(len(nums))],[0 for i in range(len(nums))]
        
        # base cases
        first_robbed_rob[0], first_robbed_rob[1] = nums[0], nums[0]
        first_robbed_norob[0], first_robbed_norob[1]  = nums[0], nums[0]
        first_norobbed_rob[0], first_norobbed_rob[1] = 0, nums[1]
        first_norobbed_norob[0], first_norobbed_norob[1] = 0, 0
        
        for i in range(2, len(nums)):
            
            # edge case, at the last house
            if i == len(nums)-1:
                # if first house is robbed, we can't rob the last house, so it's same as
                # the previous itr result
                first_robbed_rob[-1] = max(first_robbed_rob[-1], first_robbed_norob[-1])
                # if first house is not robbed, we rob the last house
                first_norobbed_rob[-1] = max(first_norobbed_rob[-3] + nums[i], first_norobbed_norob[-3] + nums[i], first_norobbed_norob[-2] + nums[i], first_norobbed_rob[-2]) 
                
            # inductive rule
            else: 
                first_robbed_rob[i] = max(first_robbed_rob[i-2] + nums[i], first_robbed_norob[i-1]+ nums[i])
                first_robbed_norob[i] = max(first_robbed_norob[i-1], first_robbed_rob[i-1])

                first_norobbed_rob[i] = max(first_norobbed_rob[i-2] + nums[i], first_norobbed_norob[i-1]+nums[i])   
                first_norobbed_norob[i] = max(first_norobbed_norob[i-1], first_norobbed_rob[i-1])
                                          
        print(first_robbed_rob, first_robbed_norob, first_norobbed_rob, first_norobbed_norob)
        return max(first_robbed_rob[-2], first_robbed_norob[-2], first_norobbed_rob[-1], first_norobbed_norob[-1])
        
        
        
        