class Solution:
    def jump(self, nums: List[int]) -> int:
        # IDEA: each jump can potentially land on the range [x, x+n], we use a greedy algorithm 
        # in which each jump we must land on the next position that has the largest jumping power. 
        # this will gurantee to work because compared to another person who only jumps as far as he can at every step,
        # the greedy solution will always yield a larger range for the person to land on. 
        
        # TIME: O(n)
        # SPACE: O(1)
        
        l = r = res = farthest = 0

        # len(nums) - 1 because as soon as we reach the second to last element, we only need to jump one more time (res+=1)
        while r < len(nums) - 1: 
            for idx in range(l, r+1): # [l,r] is the jump range, we need to find the position with max jump power
                farthest = max(farthest, idx + nums[idx])
            
            # advance the range to r+1, which is (last furthest range+1), to the current furthest range.
            l = r+1 
            r = farthest  
            res += 1
        return res
            
        
                  