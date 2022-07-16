class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # IDEA: 
        # observe that uniquePaths(x,y) = uniquePaths(x-1, y) + uniquePaths(x, y-1)
        # we can use DP: 
        # initialize a matrix D, m x n of '1's
        # for all inner cells, each inner cell (x,y) = D(x-1, y) + D(x, y-1)
        
        d = [[1 for i in range(n)] for j in range(m)]
        
        for i in range(1, len(d)):
            for j in range(1, len(d[0])):
                d[i][j] = d[i-1][j] + d[i][j-1]
                
        return d[m-1][n-1]

# Pure recursive solutions (time limit exceeded)

class Solution:
  def uniquePaths(self, m, n):
    if (m == 1 or n == 1):
      return 1 # for the first row or first column, there is always one unique path

    return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)