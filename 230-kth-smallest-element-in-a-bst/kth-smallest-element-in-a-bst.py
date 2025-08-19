class Solution(object):
    def kthSmallest(self, root, k):
            answer = [0]
            count = [k]

            def dfs(node):
                if not node:
                    return

                dfs(node.left)

                
                if count[0] == 1:   
                    answer[0] = node.val
                count[0] -= 1 
                if count[0]>0:
                    dfs(node.right)
                

            dfs(root)
            return answer[0]