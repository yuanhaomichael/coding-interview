class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # IDEA: use Counter to create a hashmap to count how many of each element there is. The key is the value
        # itself. If k==0, we try to see if there is more than 1 same element, so we can create a pair (x,x).

        # TIME: O(n)
        # SPACE: O(n)
        from collections import Counter
        result = 0

        counter = Counter(nums)

        for x in counter:
            if k > 0 and x + k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
        return result