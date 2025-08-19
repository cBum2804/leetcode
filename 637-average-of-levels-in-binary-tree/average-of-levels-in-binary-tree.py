# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return None

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            n = len(queue)
            avg = 0
            for i in range(n):
                current = queue.popleft()
                avg+=current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            avg=float(avg)/n
            res.append(avg)
        return res