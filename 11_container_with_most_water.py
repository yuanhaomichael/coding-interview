class Solution:
    def maxArea(self, height: List[int]) -> int:
        # IDEA: using two pointers at both end, keep a maxarea. For each iteration, move the shorter line 
        # inward by one step because           
        # it might be beneficial to maximizing the area. Updating the higher line would either decrease the area
        # or keep the area the same.      
        # (proof: suppose we have h[l] < h[r], and l=0, r=n-1, this is the 
        # largest container that l can help form b/c having r-=1 will only decrease the area. 
        # However, if l+=1, we can potentially increase the area)

        # TIME: O(n)
        # SPACE: O(1)
        
        l = 0
        r = len(height)-1
        maxarea = 0
        
        while l<r:
            maxarea = max(maxarea, (r-l)*min(height[l], height[r]))
            if height[l]>height[r]:
                #move r pointer's line inward 1 step
                r-=1
            else: 
                l+=1
        
        return maxarea
        