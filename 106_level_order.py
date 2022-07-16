
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

##### Approach 1: recursion ########
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        levels = []
        def helper(node, level):
            # if current level reaches a new level, create a new [] in levels
            if len(levels) == level:
                levels.append([])
            
            # apppend the current node
            levels[level].append(node.val)
            # recurse for the children
            if node.left is not None:
                helper(node.left, level+1)
            if node.right is not None:
                helper(node.right, level+1)
        
        
        helper(root, 0)
        
        return levels


####### Approach 2: BFS ##########
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q1 = [root]
        result = []
        result.append([root.val])
        while q1:
            level_result = []
            for i in range(len(q1)): 
                node = q1.pop(0)
                if node.left!=None:
                    q1.append(node.left)
                    level_result.append(node.left.val)
                if node.right!=None:
                    q1.append(node.right)
                    level_result.append(node.right.val)
            if len(level_result)!=0: 
                result.append(level_result)

        return result