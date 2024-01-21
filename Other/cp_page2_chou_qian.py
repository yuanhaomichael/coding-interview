def solution(m: int, n: int, nums: list[int]) -> bool:
    res = [False]

    def rec(sum, chances, arr):
        if len(arr) == 0:
            return
        if chances == 1 and sum in arr:
            res[0] = True
            return
      
        num = arr[0]

        # if chances is 3, use num 0,1,2,3 times, and go into recursion
        for i in range(0, chances + 1):
            rec(sum - num * i, chances - i, arr[1:])

    rec(m, 4, nums)
    return res[0]

res = solution(10, 3, [0, 1, 3, 5])
print("res:", res)
