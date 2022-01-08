class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # IDEA: 
        # if mid is greater than the left, it means that the left portion is a properly ascending arr without         
        # any pivot index and the right portion has the pivot index
        
        # if mid is less than the left, it means that the right portion is a properly ascending arr without           
        # any pivot index and the right portion has the pivot index
        
        # with this, we can do regular binary search
        
        # TIME: O(log n)
        
        l, r = 0, len(nums)-1
        
        while l<=r: # why???
            mid = l + (r-l)//2
            
            if target == nums[mid]:
                return mid
            elif nums[mid] >= nums[l]: 
                #if mid is greater than left, the left portion is properly ascending without any pivot index
                
                # because the left portion is an ascending arr, we can do regular binary search
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else: 
                    l = mid + 1
            else:
                #if mid is less than the left, the right portion is properly ascending
                
                # because the right portion is an ascending arr, we can do regular binary search
                if target <= nums[r] and target>nums[mid]:
                    l = mid+1
                else: 
                    r = mid-1
                
        return -1