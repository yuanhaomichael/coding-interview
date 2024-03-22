class MinStack:
    # if this is a state machine, at every state we have a min_element. 
    # if the current element popped is smaller or equal to the min_element,
    # we can roll back to state - 1's min_element (before this element is pushed)
    from collections import deque
    def __init__(self):
        self.last_min = deque()
        self.min_element = float('inf')
        self.stack = deque()

    def push(self, val: int) -> None:
        self.min_element = min(val, self.min_element)
        self.last_min.append(self.min_element)
        self.stack.append(val)
        
    def pop(self) -> None:
        top = self.top()
        
        if top > self.min_element:
            self.stack.pop()
            self.last_min.pop()
        else:
            self.stack.pop()
            self.last_min.pop()
            self.min_element = self.last_min[-1] if len(self.last_min) > 0 else float('inf')

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_element
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()