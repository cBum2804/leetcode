# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root is None: 
            return []

        queue = deque()
        queue.append(root)
        res =[]

        while queue:
            level = []
        
            n = len(queue)
            for i in range(n):
                current = queue.popleft()
                level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            res.append(level)
        
        return res
        