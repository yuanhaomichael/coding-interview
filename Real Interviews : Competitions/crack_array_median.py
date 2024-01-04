'''
Numbers are randomly generated and stored into an (expanding) array. 
How would you keep track of the median?
'''

import heapq, random
arr = []
minheap, maxheap = [], []
for i in range(5000):
  number = random.randrange(1, 1000)
  arr.append(number)

  # store all in a maxheap,
  # pop half of it and store it into minheap
  heapq.heappush(maxheap, -1*number)

  # bring the bigger half of the maxheap into minheap
  while abs(len(maxheap) - len(minheap)) > 1:
    heapq.heappush(minheap, -1*heapq.heappop(maxheap))
  
  median = 0
  if len(arr) % 2 == 0:
    median = (maxheap[0]*-1 + minheap[0])/2
  else:
    median = -1*maxheap[0] if len(maxheap) > len(minheap) else minheap[0]
  

  ################# Testing Harness ######################
  arr.sort()
  # print(arr, median) 
  test = 0
  if len(arr) % 2 == 0:
    test = arr[len(arr)//2] + arr[len(arr)//2-1]
    test/=2
  else:
    test = arr[len(arr)//2]

  assert(test==median)

  # put all numbers back into maxheap
  while len(minheap) > 0:
    heapq.heappush(maxheap, -1*heapq.heappop(minheap))


print("test passed")