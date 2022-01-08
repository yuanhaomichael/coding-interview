# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # IDEA: calculate the length of the linkedlist and the postion of the node from the head; traverse the list again
        
        # TIME: O(n)
        # SPACE: O(1)
        

        cur = head
        cnt = 0 
        # find number of nodes in the list
        while cur!=None:
            cnt+=1
            cur = cur.next
        
        pos = cnt - n + 1 #position of node to remove (1-indexed)
        
        # edge case: if the first node needs to be removed, return head.next
        if pos==1:
            return head.next
        
        cur1 = head
        cnt = 0
        while cur1!=None:
            cnt+=1
            if cnt==pos-1:
                # remove the node
                nextNode = cur1.next.next
                cur1.next.next = None
                cur1.next = nextNode
            cur1 = cur1.next
            
        return head
                
        
############################
# 2-pointer solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # IDEA: can maintain 2 pointers that are nth nodes apart. When the fast pointer gets to the end, the first pointer points at the nth node from the end of the list
        
        # TIME: O(n)
        # SPACE: O(1)
        
        dummy = ListNode(-1)
        dummy.next = head
        cur1 = cur2 = dummy
        
        # advance cur2 to the nth-1 position
        for i in range(n+1):
            cur2 = cur2.next

        # start advancing both pointers until cur2 reaches the end
        while cur2!=None:
            cur1 = cur1.next
            cur2 = cur2.next
             
        # remove the next node of cur1
        cur1.next = cur1.next.next
        
        return dummy.next #must return dummy.next because head may be removed
            
            
            
            
    