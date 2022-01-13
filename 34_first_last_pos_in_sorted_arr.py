class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # IDEA: use binary search to find any occurrence of the target and then keep checking left and 
        # right to find the first and last occurrence   
        
        # TIME: O(n) beacuse if the array is filled with the same number it will take linear time
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
                break
            
            elif nums[mid] > target: 
                r = mid - 1
            
            else: 
                l = mid + 1
            
        
        
        return [first, last]


    #########################
    # Second Solution
    
    class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # IDEA: use a binary search to find first occurrent and another to find last occurence. 
        # for first occ: if nums[mid-1]!=target, it means that mid is the first acc.
        # for last occ: if nums[mid+1]!=target, it means that mid is the last occ.
        
        # TIME: O(log n)
        # SPACE: O(1)
        
        # true indicates finding first occ, false indicates finding last occ
        first = self.findBound(nums, target, True)
        # if first occ doesn't exist, this target doesn't exist
        if first == -1:
            return [-1,-1]
        last = self.findBound(nums, target, False)
        
        return [first, last]
    
    def findBound(self, nums: List[int], target: int, isFirst: bool):
        n = len(nums)
        begin, end = 0, n-1
        while begin<=end:
            mid = begin+(end-begin)//2
            if nums[mid]==target:
                if isFirst:
                    # found the first occ if mid is the first of subarray or the previous number is not target
                    if mid==begin or nums[mid-1]!=target:
                        return mid
                    end = mid-1
                else: 
                    # found the last occ if mid is the end of the subarray or the next number is not target
                    if mid==end or nums[mid+1]!=target:
                        return mid
                    begin = mid+1
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid+1
            
        return -1
     