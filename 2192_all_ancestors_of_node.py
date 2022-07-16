def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    from collections import defaultdict, deque
    # IDEA: use DFS to traverse backward from leaf to its ancestors
    # TIME: O(n)
    # SPACE: O(n^2)
    # for each node, keep track of how many edges going out
    out_degree = defaultdict(int)
    # for each node, use a dic to store its ancestors
    direct_ancestor = defaultdict(list)
    # ans in the form of an array of set
    ans = [set() for _ in range(n)]
    
    # storing nodes for which we've finished a dfs 
    dfs_done = set()

    for x, y in edges:
        direct_ancestor[y].append(x)
        out_degree[x] += 1
    
    # dfs will start from each leaf node, going backwards
    q = deque()
    for i in range(n):
        if out_degree[i] == 0: 
            q.append(i)
    
    # recursive dfs
    def dfs(x):
        # if this node has already been dfs'ed, return all its ancestors
        if x in dfs_done: return ans[x]
        
        # for each ancestor of the current node x, 
        # -union OR its current ancestors with the ancestor of its ancestors
        # -add its immediate ancestor
        # -in dfs_done, mark that we've done dfs for its ancestor
        for ances in direct_ancestor[x]:
            ans[x] |= dfs(ances)
            ans[x].add(ances)
            dfs_done.add(ances)
        return ans[x]

    while q:
        dfs(q.popleft())

    return [sorted(l) for l in ans]


# APPROACH 2: BFS

class Solution:
    def getAncestors(self, n: int, edges: [[int]]) -> [[int]]:
        adjacent = [[] for _ in range(n)]
        for s, e in edges:
            adjacent[s].append(e)
        res = [set() for _ in range(n)]
        starter = [True] * n
        for s, e in edges:
            starter[e] = False
        nodes = []
        for i in range(n):
          # the initial queue has all the starter nodes
            if starter[i]:
                nodes.append(i)
        while nodes:
            node = nodes.pop(0)
            for adj in adjacent[node]:
                # for the ancestors of adj
                # it is its parent + the ancestors of its parent
                res[adj].add(node)
                for n in res[node]:
                    res[adj].add(n)

                # similar to a reached table
                if adj not in nodes:
                    nodes.append(adj)
        for i in range(len(res)):
            res[i] = list(res[i])
            res[i].sort()
        return res