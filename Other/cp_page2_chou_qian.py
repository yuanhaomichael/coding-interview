def solution(m: int, n: int, nums: list[int]) -> bool:
  # 1. naive solution
  # res = False
  # for i in nums:
  #   for j in nums:
  #     for k in nums:
  #       for l in nums:
  #         if i+j+k+l == m:
  #           res = True
  #           if res:
  #             print(i,j,k,l)

  # 2. recursion
  # base case: given m, and 1 chance, simply search in the array
  # rec(sum, array, chances)
  pass



res = solution(10, 3, [1,3,5])
# 1. (3,5) => 10
# 2. (3,5) => 10-1   10-2  10-3
print("res:", res)
