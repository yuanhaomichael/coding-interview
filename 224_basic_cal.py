class Solution:
    def calculate(self, s: str) -> int:
        # IDEA: strip the spaces first
        # keep a var called level, when I encounter a left parenthesis, I put on the stack, meaning going a level deeper
        # when I encounter a right parenthesis, I pop out of the stack, meaning going a level shallower 
        
        # keep another stack pushing in (operator, level) and (operand, level). When a right parenthesis is encountered, 
        # I pop out and compute everything on the current level, I then push onto the stack (result, level-1)
        
        # remember to keep computing the stack until it is empty at the end
        
        # TIME: O(N)
        
        def compute_cur_level(op_stack, level):
            arr = []
            while op_stack and op_stack[-1][1] == level:
                x = op_stack.pop()
                arr.append(x[0])
            arr.reverse()
            res = 0
            op = 1

            for i in range(len(arr)):
                if arr[i] != '+' and arr[i] != '-':
                    res += (op * int(arr[i]))
                elif arr[i] == '+':
                    op = 1
                elif arr[i] == '-':
                    op = -1
                    
            return res
        
        def process(s, ops):
            exp = []
            i,j = 0,0
            while i < len(s):
                if s[i] == ' ':
                    i+=1
                    continue
                elif s[i] in ops:
                    exp.append(s[i])
                else: 
                    j = i
                    num = ''
                    while j < len(s) and s[j] not in ops:
                        num += s[j]
                        j += 1
                    exp.append(num)
                    i = j
                    continue
                i+=1
            return exp
            
        from collections import deque
        ops = {'+', '-', '(', ')'}
        exp = process('0' + s if s[0] == '-' else s, ops)
        # print(exp)
        op_stack = deque()
        level = 0
        for i in range(len(exp)):
            if exp[i] == '(':
                level += 1
            elif exp[i] == ')':
                cur_res = compute_cur_level(op_stack, level)
                level -= 1
                op_stack.append((cur_res, level))
            else: 
                op_stack.append((exp[i], level))
        
        return compute_cur_level(op_stack, 0)
        
        
    
    
        
#### Recursive Approach


class Solution {
    int i;

    public int calculate(String s) {

        int operand = 0;
        int result = 0; // For the on-going result
        int nextOperandSign = 1;  // 1 means positive, -1 means negative

        while(i < s.length()) {

            char ch = s.charAt(i++);

            if (ch == ' ' || Character.isDigit(ch)) {
                operand = (ch == ' ') ? operand : 10 * operand + (ch - '0');
                
            } else if (ch == '(') {
                operand = calculate(s);
                
            } else if (ch == ')') {
                break; // Sub-expression we were evaluating has ended. Exit now...
                
            } else { 
                // If we're here, we just read the operator for the next operand/expression.
                // Evaluate the existing expression already read, reset operand, set sign for next incoming operand.
                result += nextOperandSign * operand;
                nextOperandSign = ch == '+' ? 1 : -1;
                operand = 0;
            }
        }

        return result + (nextOperandSign * operand);
    }
}



#### Approach 3, stack and no string reversal

class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative  

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand