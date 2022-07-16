class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # insertion sort
        for i in range(1, len(nums)):
            # IDEA: for each item, check back to insert it at the right position
            # TIME: O(n^2)
            # SPCAE: O(1)
            val = nums[i]
            j = i - 1
            while j >= 0 and val < nums[j]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
                j-=1
        return nums

x = Solution()
print(x.sortArray([5,4,3,2,1]))