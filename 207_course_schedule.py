
# DFS Post Order Traversal
class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        # rep the graph
        from collections import defaultdict
        graph = defaultdict(list) # each course, document all outgoing courses. Cur is the prereq
        
        for x,y in prereq: 
            graph[y].append(x)
            
        # detect if there is cycle in the graph
        def has_cycle(reached, node):
          # check if current node has been checked before, if checked, it means that it has no cycle
            if checked[node]:
                return False
            if reached[node]:
                return True
            
            reached[node] = True
            
            # backtrack
            ret = False
            for child in graph[node]:
                ret = has_cycle(reached, child)
                if ret: break
                    
            reached[node] = False
            # mark the current node as checked after visiting all child nodes
            checked[node] = True
            return ret
        
        reached = defaultdict(int)
        checked = defaultdict(int)
        for i in range(numCourses):
            if has_cycle(reached, i):
                return False
      
        return True





##############################################
# backtracking, cannot pass all test cases
class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        # rep the graph
        from collections import defaultdict
        graph = defaultdict(list) # each course, document all outgoing courses. Cur is the prereq
        
        for x,y in prereq: 
            graph[y].append(x)
            
        # detect if there is cycle in the graph
        def has_cycle(reached, node):
            if reached[node]:
                return True
            
            reached[node] = True
            
            # backtrack
            ret = False
            for child in graph[node]:
                ret = has_cycle(reached, child)
                if ret: break
                    
            reached[node] = False
            return ret
        
        reached = defaultdict(int)
        for i in range(numCourses):
            if has_cycle(reached, i):
                return False
      
        return True