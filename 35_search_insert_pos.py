class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # IDEA: use binary search, if target isn't found, then return the left pointer + 1
        # TIME: O(log(n))
        # SPACE: O(1)
        l, r = 0, len(nums)-1
        
        while l<=r: # why???
            mid = l+(r-l)//2
            
            if target == nums[mid]:
                return mid
            
            elif target > nums[mid]:
                l = mid+1
            
            else: 
                r = mid-1
        
        # why ???
        if l>r:
            return r+1
        else: 
            return l+1