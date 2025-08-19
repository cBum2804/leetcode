# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        good_nodes = 0
        stack = [(root,float('-inf'))]

        while stack:
            node, largest = stack.pop()
            
            if largest<=node.val:
                good_nodes+=1
            
            largest =max(largest, node.val)

            if node.left:
                stack.append((node.left, largest))
            if node.right:
                stack.append((node.right, largest))

        return good_nodes
        