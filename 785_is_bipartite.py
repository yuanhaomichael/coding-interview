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
        red_nodes = set()
        black_nodes = set()
        
        for i in range (len(graph)):
            if i not in red_nodes or i not in black_nodes:
                queue = deque([i])
        
                while queue:
                    node = queue.popleft()
                    if node in red_nodes:
                        red_node = True
                    else:
                        red_node = False

                    for n in graph[node]:
                        if n in red_nodes and red_node:
                            return False

                        if n in black_nodes and not red_node:
                            return False

                        if n not in black_nodes and n not in red_nodes:
                            if red_node:
                                black_nodes.add(n)
                            else:
                                red_nodes.add(n)

                            queue.append(n)
                    
        return True