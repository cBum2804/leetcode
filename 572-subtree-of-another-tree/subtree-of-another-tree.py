# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def sameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!= q.val:
                return False
            else:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        def subtree(root):
            if root is None:
                return False
            if sameTree(root, subRoot):
                return True
            
            return subtree(root.left) or subtree(root.right)
        
        return subtree(root)
        