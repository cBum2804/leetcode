# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        answer = [0]
        count = [k]

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            count[0] -= 1
            if count[0] == 0:   # found kth smallest
                answer[0] = node.val
                return

            dfs(node.right)

        dfs(root)
        return answer[0]


        
        