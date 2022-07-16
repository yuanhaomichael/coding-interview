class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # IDEA: get the sum of the array, which is the diff between the begin and the end of the hidden. 
        # get the smallest cumulative sum and largest, check range 
        # TIME: O(n)
        # SPCAE: O(1)        
        
        begin_end = sum(differences)
        if begin_end > upper-lower:
            return 0
        
        # find the smallest cumulative sum and the biggest cumulative sum, because they may cause hidden
        # array to go out of range
        smallest_sum = biggest_sum = 0
        sum1 = 0
        for i in differences:
            sum1+=i
            smallest_sum = min(smallest_sum, sum1)
            biggest_sum = max(biggest_sum, sum1)
            
        lowest_begin = lower+ -1*smallest_sum
        biggest_begin = upper - biggest_sum


        # need to check if all nums in hidden array is within the lower and upper range
        if biggest_begin < lowest_begin:
            return 0
        
        return biggest_begin-lowest_begin+1