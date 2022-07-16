class Solution:
    def candy(self, ratings: List[int]) -> int:
        # IDEA: traverse the ratings array, if the next item is higher, increment the cur_candy by 1
        # because the ratings array if it's continuously increasing, the candy array will be as well, just in a more
        # "low cost" way, meaning only incrementing one by one. 
        
        # When doing the backward pass, if incrementing results in conflict with the original candy count set during the 
        # forward pass, we take the max(candy_arr[i], cur_candy) because that will follow the rule that higher rating
        # neighbor has more candy. 
        
        # TIME: O(N)
        
        arr = [1 for i in ratings]
        
        cur_candy = 1
        # forward pass
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                cur_candy+=1
                arr[i] = cur_candy
            elif ratings[i] <= ratings[i-1]:
                cur_candy = 1
        
        # backward pass
        supposed_candy = 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                supposed_candy += 1
                arr[i] = max(arr[i], supposed_candy)
            elif ratings[i] <= ratings[i+1]:
                supposed_candy = 1
                arr[i] = max(arr[i], supposed_candy)
                
        return sum(arr)
                
        
        
            
        