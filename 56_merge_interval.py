
# Best Approach:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        merged = []
        
        for inter in intervals:
            if len(merged) == 0 or inter[0] > merged[-1][1]:
                # an interval that has nothing to do with prev intervals
                merged.append(inter)
                
            else:
                merged[-1][1] = max(merged[-1][1], inter[1])
                
        return merged
        












# My approach
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        while len(intervals) != 0:
            # merge with intervals later on until there is no other intervals to merge, while popping the intervals array
            merged = intervals[0]
            intervals.pop(0)
            while len(intervals) > 0 and intervals[0][0] <= merged[1]:
                # keep merging
                merged = [min(merged[0], intervals[0][0]), max(merged[1], intervals[0][1])]
                intervals.pop(0)
            
            res.append(merged)
            
        return res
                
            
            
                
            