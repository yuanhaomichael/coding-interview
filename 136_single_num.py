class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # IDEA: a XOR a = 0 and 0 XOR b = b. So we XOR everything to 
        # get the unique number. 
        
        # TIME: O(n)
        # SPACE: O(1)
        a = 0
        for i in nums:
            a^=i
            
        return a