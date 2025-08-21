class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        order_list = []
        edges = defaultdict(list)

        for i, j in prerequisites:
            edges[i].append(j)
        
        UNVISITED,VISITING, VISITED = 0,1,2
        states = [UNVISITED]*numCourses

        def dfs(node):
            
            state = states[node]
            if state == VISITING: return False
            elif state == VISITED: return True

            states[node] = VISITING

            for x in edges[node]:
                if not dfs(x):
                    return False
            states[node]= VISITED
            order_list.append(node)
            return True    
                    


        for i in range(numCourses):
            if not dfs(i):
                return []

        return order_list        