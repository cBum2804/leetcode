# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        def isEqualNode(p,q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val!= q.val:
                return False
            
            else:
                return isEqualNode(p.left, q.left) and isEqualNode(p.right, q.right)
            
        return isEqualNode(p,q)
        