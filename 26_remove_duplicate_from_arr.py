class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #IDEA: use 2 pointers, l is slow, r is fast, if values at l and r are not equal, then increment l by 1 and let nums[l] = nums[r]
        #TIME: O(n) 
        #SPACE: O(1) because it's in place
        
        if len(nums) == 0:
            return 0
        
        l = 0
        
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                l+=1
                nums[l] = nums[r]
            
        return l+1