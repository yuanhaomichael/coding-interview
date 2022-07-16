class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # IDEA: town judge has n-1 incoming edges and no outgoing edges. 
        # collect incoming edges and outgoing edges for each node from 1 to N and return if 
        # we see a satisfying node. 

        # TIME: O(n)
        # SPACE: O(n)
        
        if len(trust)==0 and n==1:
            return 1
        dic = {}
        dic_distrust = set()
        for item in trust:
            trusted = item[1]
            dic_distrust.add(item[0])
    
            if trusted in dic:
                dic[trusted]+=1
            else:
                dic[trusted] = 1
        
        for key in dic:
            if dic[key]==n-1 and key not in dic_distrust:
                # check if it trust no one
                return key
        return -1


  # Approach 2

class Solution(object):
  def findJudge(self, N, trust):
      # IDEA: town judge's node has no outgoing and n-1 incoming edges. #Incoming-#outgoing = n-1. So use this to 
      # count this metric for each node
      count = [0] * (N + 1)
      
      for i, j in trust:
          count[i] -= 1
          count[j] += 1
          
      for i in range(1, N + 1):
          if count[i] == N - 1:
              return i
          
      return -1