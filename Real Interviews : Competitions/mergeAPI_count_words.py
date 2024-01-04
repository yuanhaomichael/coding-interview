'''
Given a pool of letters in upper case and a list of words in upper case, find what is the max number of any word 
we can form with the pool of letter. 

eg. 
"ABCABCABC" ['ABC', 'B', 'AAA']
In this case, we can form 3 'ABC', 3 'B', and 1 'AAA' with the word pool, so we return 3.

"ABC" ['Z', 'DA'] we return 0
'''

from collections import Counter
def solution(S, L):
  s = Counter(S)
  res = -1
  for word in L:
    dic = Counter(word)
    number = 0
    if len(word) <= len(S):
      min1 = 1000
      for letter in dic:
        x = s[letter] // dic[letter]
        if x < min1:
          min1 = x
      number = min1
    
    if number > res:
      res = number
  return res

        
x = solution('BILLBILLXYZ', ['BILL', 'XYZ'])
print(x)