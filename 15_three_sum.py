class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #IDEA: pin nums[i] as the first element of the result triplet, then go through the 2-pointer process
        #to find a pair of values that sums up to the target
        
        #TIME: O(n^2) because 2 loops
        #SPACE: O(1)
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            # because array is sorted, once nums[i] greater than 0, don't need to go through the 2 pointer process because result will always be positive
            if nums[i] > 0:
                break
            target = -nums[i]
            
            l = i + 1
            r = len(nums) - 1
            
            if i==0 or nums[i-1] != nums[i]: #check to make sure the previous nums[i] is not the same as current nums[i] to remove duplicates
                #we go through the 2 pointer process to find the 2 values that sum up to the target
                while l<r: 
                    sums = nums[l]+nums[r]
                    if sums == target:
                        res.append([nums[i],nums[l],nums[r]])
                        r-=1
                        l+=1
                        # in the case of [-2, 0, 0, 2, 2], there will be potentially 2 pairs of [-2,0,2], we need to get rid of duplicates
                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                    elif sums < target:
                        l+=1
                    elif sums > target:
                        r-=1
        return res