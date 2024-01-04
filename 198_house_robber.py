class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # IDEA: 
        # if i rob the current house, check prev prev house max amount + cur house
        # if i don't rob, check prev house max amount
        
        # DP tricks
        # 1. Find the inductive rule
        
        # 2. Start with the base cases
        if len(nums) <= 2:
            return max(nums)
        
        # 3. Initialize the base cases
        # rob = [nums[0], nums[1]]
        # no_rob = [0, nums[0]]
        
        pp_rob, p_rob = nums[0], nums[1]
        
        pp_norob, p_norob = 0, nums[0]
        
        
        # 4. Loop through the array and code the inductive rule
        # If don't rob the current house, no_rob[i] = max(rob[i-1], no_rob[i-1])
        # If rob the current house, rob[i] = max(rob[i-2] + nums[i], no_rob[i-2] + nums[i])
        for i in range(2,len(nums)):
            temp_p_norob, temp_p_rob = p_norob, p_rob
            p_norob = max(p_rob, p_norob)
            p_rob = temp_p_norob + nums[i]
            pp_norob, pp_rob = temp_p_norob, temp_p_rob
        
            
        return max(p_rob, p_norob)
                   
        # 5. Runtime? Memory? Any room for optimization?
        # O(N)
    
