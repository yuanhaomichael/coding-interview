# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        q = [(root, 1)]
        dic = {}
        h = 0
        while q:
            node, h = q.pop(0)
            
            x = node.val if node is not None else None
            if h not in dic:
                dic[h] = [x]
            else: 
                dic[h].append(x)
                
            if node != None:
                q.append((node.left, h+1))
                q.append((node.right, h+1))
                
        for i in range(1, h):
            arr = dic[i]
            for j in range(0, len(arr)//2):
                if arr[j] != arr[len(arr)-j-1]:
                    return False
        
        return True
        
###########
# Approach 2: recursive


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def reflection(a, b):
            # 2 trees are reflection if:
            
            # 1) the root of both trees are equal
            # 2) left subtree of first tree is a reflection of right subtree of second tree
            # 3) right subtree of first tree is a reflection of left subtree of second trees
            # base case when each tree root is the leaf
            if a==None and b==None: # when two root is none
                return True
            elif a==None or b==None: # when either is none
                return False
            return reflection(a.left, b.right) and reflection(a.right, b.left) and a.val == b.val
        
        return reflection(root.left, root.right)
            