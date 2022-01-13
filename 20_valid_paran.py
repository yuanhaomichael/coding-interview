class Solution:
    def isValid(self, s: str) -> bool:
        # IDEA: use a stack, when encounter left paranthesis, push onto the stack, 
        # when encounter right, pop. If a right does not correspond to the left one, then not valid.
 
        # TIME: O(n)
        # SPACE: O(n)
        dic = {')':'(', '}':'{', ']':'['}
        left = ['(','{','[']
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
                continue
                
            if c in dic and len(stack)>0 and dic[c] == stack[len(stack)-1]:
                stack.pop()
            else:
                return False
        
        
        if len(stack) > 0:
            return False
        
        return True
                
                