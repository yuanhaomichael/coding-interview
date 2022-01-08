class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # IDEA: 1) find the last instance of ascending (index i as the "peak position"), if no ascending at all, return reversed str
        # 2) j = i-1. find smallest number x after j such that nums[j] < x <= nums[i]. Swap indexOf(x) and j
        # 3) sort all nums after indexOf(x) in ascending order
        
        # TIME: O(n)
        # SPACE: O(1)
        
        # find the last instance of ascending (from the back, the first instance of descending)
        i = len(nums)-1
        while i>=1:
            if nums[i]>nums[i-1]:
                break
            i-=1
        if i==0:
            nums.reverse()
            return
        
        j = i-1
        # find smallest number x after j such that nums[j] < x <= nums[i]. Swap indexOf(x) and j
        x = nums[i]
        x_index = i
        for m in range(j,len(nums)):
            if nums[m] <= nums[i] and nums[m] > nums[j]:
                x_index = m
                x = min(x, nums[m])
        
        # swap x_index with j
        nums[x_index] = nums[j]
        nums[j] = x
        
        # sort all nums after x_index in ascending order
        nums[j+1:] = sorted(nums[j+1:])
        
        