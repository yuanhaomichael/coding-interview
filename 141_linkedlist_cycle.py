# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # IDEA: 2 pointers l and r, if when both pointers proceed to the same node
        # it means that there is a cycle. 
        
        # l pointer moves 1 step at a time, r pointer moves 2 steps at a time
        # eventually, if there is a cycle, the 2 must land on the same node. 

        # TIME: O(n)
        # SPCAE: O(1)
        if head == None:
            return False
        l = r = head
        while True:
            if r==None:
                return False
            elif r.next==None:
                return False
            l = l.next
            r = r.next.next
            if l==r:
                return True
        
            