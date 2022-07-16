
# Recursion
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def helper(tmp, toOpen, toClose):
            if toOpen == 0 and toClose == 0:
                result.append(tmp)
                return
            
            if toOpen > 0:
                # if ( hasn't been added, add 1 at a time
                helper(tmp + '(', toOpen - 1, toClose + 1)
            if toClose > 0:
                # if we have ) left, we add ) 1 at a time
                helper(tmp + ')', toOpen, toClose - 1)
        

        helper('', n, 0)
        
        return result
    



# backtrack

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S=[], left=0, right=0):
            if len(S) == 2*n:
                ans.append("".join(S))
                return
            if left<n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right<left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans