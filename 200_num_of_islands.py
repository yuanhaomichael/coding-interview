class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # IDEA: go through every point, do BFS, mark as searched if we traverse a point (so don't need to visit
        # later on). BFS ending condition is when all possible neighbors are visited already
        
        # TIME: O(MN)
        def bfs(x, y, visited, m,n):
            from collections import deque
            q = deque([(x,y)])
            while q:
                (x,y) = q.popleft()
                neighbors = [(-1,0), (1, 0), (0,1), (0,-1)]
                for (offset_y, offset_x) in neighbors:
                    new_y = y+offset_y
                    new_x = x+offset_x
                    if new_y in range(0,m) and new_x in range(0,n) and (new_x, new_y) not in visited and grid[new_y][new_x]=='1':
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y))        
        
        visited = set()
        m = len(grid)
        n = len(grid[0])
        res = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    if (x, y) in visited:
                        continue
                    else:
                        visited.add((x,y))
                        bfs(x, y, visited,m,n)
                        res += 1
        return res
                    
            
                        
            
            