class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # find T such that T//t[0] + T//t[1] + ... T//t[n-1] = x 
        lo, hi = 1, 10 ** 15

        def f(mid):
            return sum(mid // t for t in time) >= totalTrips

        while lo < hi:
            mid = (lo + hi) // 2
            if f(mid): hi = mid   # search left
            else: lo = mid + 1 # search right
        return lo