class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # IDEA: use binary search to find the first occurrence of the target and then keep checking right to find the last occurrence   
        
        # TIME: O(log(n))
        # SPACE: O(1)
        l, r = 0, len(nums)-1
        first = -1
        last = -1
        
        # traverse left to find first occurrence
        def findFirst(mid):
            i = mid
            while i >= 0:
                if nums[i] != nums[i-1] or i==0:
                    return i
                i-=1
        
        # traverse right to find last occurrence
        def findLast(mid):
            for i in range(mid, len(nums)-1):
                if nums[i] != nums[i+1]:
                    return i
            return len(nums)-1
                
            
        # normal binary search
        while l<=r: # why <= ???
            mid = l+(r-l)//2
            
            if nums[mid] == target:
                first = findFirst(mid)
                last = findLast(mid)
                print(mid, first, last)
                break
            
            elif nums[mid] > target: 
                r = mid - 1
            
            else: 
                l = mid + 1
            
        
        
        return [first, last]