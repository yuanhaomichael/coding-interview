n = int(input())
flag = False
matrix = []

for i in range(n):
  s = input()
  s = s.replace('.', '0').replace('#', '1')
  arr = [int(c) for c in s]
  # check if the row works
  for j in range(n - 6 + 1):
    window = arr[j:j+6]
    if sum(window) >= 4:
      flag = True
      #print(1)
  matrix.append(arr)

# check if columns works
for i in range(n):
  col = []
  for j in range(n): 
    col.append(matrix[j][i])
  
  for j in range(n - 6 + 1):
    window = col[j:j+6]
    if sum(window) >= 4:
      flag = True

  
  
for i in range(n):
  if n - i >= 6:
    # upper diag
    y, x = 0, i
    sum1 = []
    for j in range(n - i):
      sum1.append(matrix[y][x])
      y += 1
      x += 1
      # lower diag
    y, x = i, 0
    sum2 = []
    for j in range(n - i):
      sum2.append(matrix[y][x])
      y += 1
      x += 1
      
    for j in range(n - i):
      window1 = sum1[j:j+6]
      window2 = sum2[j:j+6]
      if sum(window1) >= 4 or sum(window2) >= 4:
        #print(3)
        flag = True
        break
    
  
# check all anti-diagonals
for i in range(n):
  if n - i >= 6:
    # upper diag
    y, x = 0,  n - 1 - i
    sum1 = []
    for j in range(n - i):
      sum1.append(matrix[y][x])
      y += 1
      x -= 1
    # lower diag
    y, x = i, n - 1
    sum2 = []
    for j in range(n - i):
      sum2.append(matrix[y][x])
      y += 1
      x -= 1
    for j in range(n - i):
      window1 = sum1[j:j+6]
      window2 = sum2[j:j+6]
      if sum(window1) >= 4 or sum(window2) >= 4:
        #print(3)
        flag = True
        break

if flag:
  print("Yes")
else: 
  print("No")











  
  
  
  
  
  
  
  
  
  
  