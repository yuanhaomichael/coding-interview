class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # IDEA: use backtracking to find all combos. Base case is when path_sum == target. Sort the path elements before 
        # adding it to the result hashset. 
        
        # TIME: T is target and M is minimum value in "candidates", O(N^(T/M)*N). There are a total of N^(T/M) operations.             # Each iteration we need to copy the path array so it will incur an N operations for each iteration. 
        
        # SPACE: call stack memory takes up O(T/M) because we can keep on adding to path the smallest values (eg. 1,1,1,1)
        # in addition, combination of numbers in path take up T/M as well
        
        res = set()
        
        def backtrack(path, path_sum):
            # if path_sum equals target, then sort the current path and add it to the result hashset
            if path_sum == target:
                arr = path.copy()
                arr.sort()
                res.add(tuple(arr))
                
            elif path_sum < target:
                for i in candidates:    
                    path_sum+=i
                    if path_sum <= target:
                        path.append(i)
                        backtrack(path, sum(path))
                        path.pop()
                    path_sum-=i
            
        backtrack([], 0)
        return res