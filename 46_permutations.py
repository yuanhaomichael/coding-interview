class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # IDEA: use backtracking, each step we get hold of a position in nums (nums[pos]) and try switching it 
        # to all possible positions.
        # TIME: O(n*n!), n! permutations, and to arrive at each permutations, there are n recursive calls made. 
        # SPACE: O(n!) because we have to store n! solutions
        
        output = []

        def backtrack(pos):
            # if all numbers are used up
            if pos == len(nums):
                output.append(nums[:])
            for i in range(pos, len(nums)):
                #place ith integer pos in the current permutation
                nums[pos], nums[i] = nums[i], nums[pos]
                
                #use next integers to complete permutations
                backtrack(pos+1)
                #backtrack
                nums[pos], nums[i] = nums[i], nums[pos]
                
           
        backtrack(0)
        return output

            