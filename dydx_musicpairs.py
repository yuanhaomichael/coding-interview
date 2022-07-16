'''
Given a list of numbers, find all pairs that sum up to multiples of 60. Give an O(n) solution. 

eg. [10, 50, 60] returns 1 because 10 and 50 sums up to 60

1 <= list[i] <= 500
'''
######## Approach 1 $############
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # if a % 60 = 0, find b % 60 = 0
        # else, find b % 60 = 60 - a%60
        
        res = 0
        from collections import defaultdict
        dic = defaultdict(int) # has entries 0-60 which we need
        
        for t in time:
            # for each number in time
            if t % 60 == 0:
                # find b such that b % 60 == 0
                res += dic[0]
            else:
                # find b % 60 = 60 - a%60
                res += dic[60 - t%60]
                
            dic[t%60] += 1
            
        return res

######### Approach 2 ###########
from collections import Counter
def solution(arr):
  # for each number, find its complement. 
  dic = Counter(arr)
  arr_set = set(arr)
  reached = set()
  cnt = 0
  for i in range(len(arr)):
    # for each number in the array, iterate all possible "other" number that sums up 
    # to multiple of 60 with the current number
    for j in range(20):
      target = j*60
      other = target - arr[i]
      if other >= 1 and other <= 500 and other in arr_set:
        pair = (arr[i], other) if  arr[i] <= other else (other, arr[i])

        # if the 2 complement are the same number, we need to make sure that dic[num] > 1
        if arr[i] == other and dic[other] <= 1:
          continue
        
        # for each pair, if we considered this pair before, we do not need to consider again
        # we use a reached table to identify if we've considered this pair before. 
        if pair not in reached:
          increment = dic[arr[i]] * dic[other] if arr[i] != other else (dic[other]*(dic[other]-1))//2
          cnt += increment
        reached.add(pair)
  return cnt




 

############# test #############
solution([0,120, 60, 60, 60])

# how do we count non-unique music pairs?
