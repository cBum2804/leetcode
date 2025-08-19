# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def pathSum(root,currSum):
            if not root:
                return False
            currSum+= root.val

            if not root.left and not root.right:
                return currSum == targetSum
            
            return pathSum(root.left, currSum) or pathSum(root.right, currSum)
        return pathSum(root, 0)
        