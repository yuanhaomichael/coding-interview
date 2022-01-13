class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # IDEA: use binary search, if target isn't found, then return the left pointer 
        # TIME: O(log(n))
        # SPACE: O(1)
        l, r = 0, len(nums)-1
        
        while l<=r: 
            mid = l+(r-l)//2
            
            if target == nums[mid]:
                return mid
            
            elif target > nums[mid]:
                l = mid+1
            
            else: 
                r = mid-1
        
        return l 
        # we return l if the target is not found because by the time the loop ends, if target>nums[mid],
        # l will have moved 1 to the right of mid. This is exactly where we need to insert target. 
        # if target < nums[mid], when loop ends, l=r=mid, target should also be inserted at position l.  