class Solution:
    def findClosestElements(self, array: List[int], k: int, target: int) -> List[int]:
        # IDEA: find the two closest elements first using binary search, then
        # expand outwards to find the k closest
        
        # TIME: O(log n + k)
        # SPACE: O(1)
        
        res = []

        l,r = 0, len(array)-1

        while l<r-1: # l neighbor r ensures the ending condition when l and r are next to one another
            mid = l+(r-l)//2
            # reduce search scope, if target==array[mid], we can reduce the scope with an extra check
            if target == array[mid]:
                if abs(array[mid-1]-target) <= abs(array[mid+1]-target):
                    r = mid
                else:
                    l = mid
            elif target < array[mid]:
                r = mid
            else:
                l = mid

        # l and r has the indices of the 2 closest elements
        cnt = 0
        # expand outwards and append whichever is closer to the target
        while l>=0 and r<=len(array)-1 and cnt<k:
            if abs(array[l]-target)<=abs(array[r]-target):
                res.append(array[l])
                l-=1
            # this is else if because once the first condition goes in, we don't want to go in this condition 
            elif abs(array[l]-target)>abs(array[r]-target):
                res.append(array[r])
                r+=1

            cnt+=1
        # post process by adding the rest of the k elements if either l or r goes out of bound
        if l<0 and cnt<k:
            while r<=len(array)-1 and cnt<k:
                res.append(array[r])
                r+=1
                cnt+=1
        if r>len(array)-1 and cnt<k:
            while l>=0 and cnt<k:
                res.append(array[l])
                l-=1
                cnt+=1

        return sorted(res)        