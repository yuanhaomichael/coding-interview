class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # IDEA: store digit to letters in a dict, use backtracking go over all possible combinations. 
        # The backtracking function takes 2 inputs, the current combination of letters we already have, 
        # and the next index we are checking. For the base case, if our current combination has the same 
        # length as our input digits, then this path is completed -- we add it to our answer array and backtrack
        #  to the previous junction. 

        # TIME: it costs worse case 4 potential branches for each letter, and for each path, it costs N to build the string
        # so O(4^n * n)

        # SPACE: O(n) because the recursion stack would occupy at most n digit space
   
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        if len(digits)==0:
            return []
        
        ans = []
        def backtrack(index, path): 
            # base case: if length of current path == length of input digits, we add it to the answer array
            if len(path) == len(digits):
                ans.append("".join(path)) # path is an array, so we must join it first
                return
                
            # get the letters that the current digit maps to, and loop through them
            # to build the backtracking tree
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index+1, path) # move to next digit
                #remove the letter just appended to return to the previous junction (parent in the backtracking tree)
                path.pop() 
        
        # initiate the backtracking recursion with index 0 and empty path
        backtrack(0, [])
        return ans







    #############################
    # DFS Solution

    class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mappings = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    
        length = len(digits)
        combinations = []
        
        def dfs_util(index, curr_word):
            if index == length:
                combinations.append(curr_word)
                return
            
            digit = digits[index]
            
            for ch in mappings[digit]:
                curr_word += ch
                dfs_util(index + 1, curr_word)
                curr_word = curr_word[:-1] #pop to backtrack to the previous root
        dfs_util(0, "")
        return combinations