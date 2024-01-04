# https://atcoder.jp/contests/abc240/tasks/abc240_c


n,x = map(int, input().split(" "))
memo = {0}

for i in range(n):
    a,b = map(int, input().split(" "))
    memo_new = set()
    for j in memo:
    # print(j)
      if j+a <= x:
        memo_new.add(j+a)
      if j+b <= x:
        memo_new.add(j+b)
    #print(memo_new)
    memo = memo_new
  
if x in memo:
  print("Yes")
else:
  print("No")
    
  
    
  
  
    
  
  



  
 

