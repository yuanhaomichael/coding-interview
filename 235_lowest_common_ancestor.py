# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # recursive subproblem: given a tree root, and 2 nodes, 
        # if base cases are met, the root is the lowest common ancestor
        # else: do the same problem for root.left and root.right


        def recursion(tree, node1, node2):
            if node1.val < tree.val and node2.val > tree.val:
                return tree
            elif node1.val > tree.val and node2.val < tree.val:
                return tree
            else:
                if node1 == tree or node2 == tree:
                    return tree
                elif node1.val > tree.val:
                    return recursion(tree.right, node1, node2)
                elif node1.val < tree.val:
                    return recursion(tree.left, node1, node2)


        res = recursion(root, p, q)
        return res

