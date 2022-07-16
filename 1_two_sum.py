class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #IDEA: use a hashmap to store {my value: my index}
        #TIME: O(n)
        #SPACE: O(n)
        
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            
            hashmap[nums[i]] = i