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
        res = ListNode(0)
        res_pt = res
        carry = 0
        
        while cur1 or cur2:
            cur1_val = cur1.val if cur1 else 0
            cur2_val = cur2.val if cur2 else 0
            
            s = cur1_val + cur2_val + carry
            
            carry = 1 if s >= 10 else 0
            
            res_pt.next = ListNode(s % 10)
            res_pt = res_pt.next
            cur1 = cur1.next if cur1 else cur1
            cur2 = cur2.next if cur2 else cur2

        if carry==1:
            res_pt.next = ListNode(1)
    
        return res.next
        