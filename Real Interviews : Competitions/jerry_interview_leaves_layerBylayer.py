# Print the leaves of a binary tree layer by layer

#   3
# 4    6
#  5  8  9
# Will print [5,8,9] [4,6] [3]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def layerBylayer(self, root):
    dic = {}

    def buildDic(root):
      if not root:
        return -1
      else:
        left = buildDic(root.left)
        right = buildDic(root.right)
        if not root:
          dic[root] = max(left, right) + 1

    buildDic(root)
    print(dic)

s= Solution()

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(4)
s.layerBylayer(root)



