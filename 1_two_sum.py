class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #IDEA: use a hashmap to store what the current number is looking for in order to add up to the target. Format desired_num : my index
        #TIME: O(n)
        #SPACE: O(n)
        
        dic = dict()
        for i in range(len(nums)):
            if nums[i] in dic:
                return [i, dic[nums[i]]]
            else:
                dic[target-nums[i]] = i