
# IDEA: if a subarray is continuously increasing or continuously decreasing, we only take 1 number, because
# only 1 number will contribute to the wiggling.
# think graphically in terms of ups and downs.

# Solution 1
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
    
        wiggle_diff = [0] # dummy data
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff>0 and wiggle_diff[-1]!=1:
                wiggle_diff.append(1)
            elif diff<0 and wiggle_diff[-1]!=-1:
                wiggle_diff.append(-1)

        
        return len(wiggle_diff)
        

# Solution 2 
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 1
        
        wiggle = 0
        flag = 0 # 1 or -1, meaning diff between cur and prev (cur-prev)
        
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            # whenever there is a wiggle
            if diff > 0 and flag < 0:
                flag = 1
                wiggle += 1 
            elif diff < 0 and flag > 0:
                flag = -1
                wiggle += 1
            elif diff < 0:
                flag = -1
            elif diff > 0:
                flag = 1
            
        if wiggle != 0:
            return wiggle + 2
        else: 
            s = {i for i in nums}
            if len(s) == 1:
                return 1
            else: 
                return 2
