class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:

        # 1. numbers unique to each array
        # 2. numbers that appear in both arrays
        n = len(nums1)

        set1 = set(nums1)
        set2 = set(nums2)

        inter = set1.intersection(set2)

        # if intersection fills the entire array
        if len(inter) == len(nums1):
            return len(inter)

        # get numbers unique to that array
        nums1u = []
        nums2u = []

        
        for i in nums1:
            if i not in set2:
                nums1u.append(i)
        for i in nums2:
            if i not in set1:
                nums2u.append(i)

        nums1u = list(set(nums1u))
        nums2u = list(set(nums2u))

        res1 = [] # need to fill up to n/2
        res2 = [] # need to fill up to n/2

        # fill up with unique numbers
        res1 = nums1u[0:int(n/2)]
        res2 = nums2u[0:int(n/2)]
        print(res1, res2)

        # fill up with intersection numbers
        empty_spots = n - len(res1) - len(res2)
        return len(set(res1+res2)) + min(len(inter), empty_spots)


        # [1,2,3,4,5,6] [2,3,4,5,7,9]
        
