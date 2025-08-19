# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        min_dist = [float('inf')] 
        prev = [None]
         
        def dfs(root):
            if root is None:
                return
            dfs(root.left)

            if prev[0] is not None:
                min_dist[0] = min(min_dist[0], root.val-prev[0])
            
            prev[0] = root.val

            dfs(root.right)
        dfs(root)
        return min_dist[0]


            
        