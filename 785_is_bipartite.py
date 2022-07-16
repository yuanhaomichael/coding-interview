from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # IDEA: for every edge that connects between 2 nodes, the 2 nodes 
        # must be of different color. For every node x, we start from the node
        # and do BFS, going through all edges (x,v), for each v, we color it 
        # different from x. When there is an unexplored edge where the 2 nodes
        # have the same color, we return False

        # This works because we assume that every edge must connect 2 nodes of different
        # colors (definition of bipartite). When we meet a contradiction
        # we return False because the graph is no longer bipartite.

        # TIME: O(N+E)
        # SPACE: O(N)
        
       # use a hashmap to mark colors of nodes. 0 as unexplored, -1, or 1
        colors = {}
        res = True
        # mark everything as unexplored
        for i in range(len(graph)):
            colors[i] = 0
        
        # for every node: do BFS, color the neighbors, and check conditions
        for i in range(len(graph)):
            res = self.bfs(graph, i, colors)
            if res == False:
                return res
        
        return True
    
    # helper to conduct BFS and check conditions
    def bfs(self, graph, start, colors) -> bool:
        # use a q to help with BFS, color each neighbor, keep going until q is empty
        q = [start]
        while len(q)!=0:
            node = q.pop(0)
            color = 0
            # 3 statuses of a node: 0, -1, 1
            if colors[node] == 0: 
                colors[node] = -1
                color = -1
            else: 
                color = colors[node]
            nei = graph[node]
            for i in range(len(nei)):
                item = nei[i]
                # if color of neighbor item equals the color of current node
                if colors[item] == color:
                    return False
                elif colors[item] == 0:
                    colors[item] = -1*color
                    q.append(item)
                   
                
        
        
        
        