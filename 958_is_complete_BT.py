# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # IDEA: use BFS to traverse and check bubble
        # case 1: bubble in the middle of a layer
        # case 2: bubble at the right most node of a layer (not last layer)
        
        # TIME: O(n)
        # SPACE: O(n)
        flag = 0
        
        q = [root]
        
        while q:
            node = q.pop(0)
            
            if node.left==None:
                flag=1
            elif node.left!=None and flag==0:
                q.append(node.left)
            else: 
                return False
            
            if node.right==None:
                flag=1
            elif node.right!=None and flag==0:
                q.append(node.right)
            else: 
                return False
        return True 
            
            
  
        