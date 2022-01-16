# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
####################################
# Solution 1: BFS
class Solution(object):
  def layerByLayer(self, root):
    """
    input: TreeNode root
    return: int[][]
    """
    # IDEA: use BFS and maintain a level count in the queue. If it's in a new level, store result in a new sublist in res. 
    # TIME: O(n)
    # SPACE: O(n) because the queue will store at most the last level of nodes of the BT, which is  n/2+1 nodes
    if root==None:
      return []

    res = []
    q = [(root,1)]
    prev_level = 0

    while len(q)!=0:
      # for each time, expand the current node, and add its children onto the q
      node, level = q.pop(0)
      if prev_level < level: #if it's a new level, add a new empty sublist in res
        res.append([])
      res[len(res)-1].append(node.val)
      # make sure to update the prev_level
      prev_level = level

      if node.left!=None:
        q.append((node.left, level+1))
      if node.right!=None:
        q.append((node.right, level+1))
    
    return res


####################################
# Solution 2: Recursion

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def layerByLayer(self, root):
    """
    input: TreeNode root
    return: int[][]
    """
    if root==None:
      return []
    res = []
    def helper(node, level): # in nested functions, no need to pass the self parameter
      if node==None:
        return 
      if len(res)==level:
        # this means we reached a new level when length of result arr == current level
        res.append([])
      # append the current node value onto the sublist res[level], which is the sublist corresponding to the current level
      res[level].append(node.val)

      # recursive calls
      helper(node.left, level+1)
      helper(node.right, level+1)

    helper(root, 0)
    return res


