class Solution(object):
  def searchInsert(self, array, target):
    """
    input: int[] input, int target
    return: int
    """
    # IDEA: 
    # TIME: O(log(n))
    # SPACE: O(1)    
    if len(array) == 0:
      return 0

    l, r = 0, len(array)-1
    # l5  x r6   --> if target == array[l], return l ; if target > array[l], return l+1
    while l<r-1: 
      mid = l+(r-l)//2
      # if target exists, we want to find the first occ
      if target == array[mid]:
        r = mid 
      elif target < array[mid]:
        r = mid  
      else: 
        l = mid

    if target == array[l]:
      return l
    elif target > array[l] and target < array[r] or target == array[r]:
      return r
    elif target > array[r]:
      return r+1
    else:
      return 0