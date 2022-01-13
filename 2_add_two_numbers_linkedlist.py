# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # IDEA: align the two linkedlist and use 2 pointers to traverse
        # while creating a result linkedlist. Carry gets added to the next             
        # iteration
        
        # TIME: O(n)
        # SPACE: O(n)
        
        cur1 = l1
        cur2 = l2
        
        carry = 0
        res = ListNode()
        res_pt = res
        while cur1!=None or cur2!=None:
            value = 0
            if carry == 1:
                value+=1
            if cur1!=None:
                value+=cur1.val
            if cur2!=None:
                value+=cur2.val
            
            if value>=10:
                value -=10
                carry = 1
            else: 
                carry = 0
             
            res_pt.next = ListNode(value)
            res_pt = res_pt.next
            
            # cur1, cur2 will eventually become none, then the loop stops
            # must check whether cur1 or cur2 = None, otherwise None.next
            # will occur
            if cur1!=None:
                cur1 = cur1.next
            if cur2!=None:
                cur2 = cur2.next
        
        if carry==1:
            res_pt.next = ListNode(1)
        return res.next
            
        