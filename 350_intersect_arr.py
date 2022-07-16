class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        
        i=j=0
        k = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i]>nums2[j]:
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                nums1[k] = nums1[i]
                i+=1
                j+=1
                k+=1
        
        return nums1[:k]


# Approach 2

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        
        dic = Counter(nums2)
        
        res = []
        for i in nums1:
            if i in dic and dic[i] > 0:
                res.append(i)
                dic[i]-=1
        
        return res