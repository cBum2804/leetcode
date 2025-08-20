class Solution(object):
    def validPath(self, n, edges, source, destination):
        if source== destination:
            return True
        seen = set()
        stack = []
        stack.append(source)
        seen.add(source)

        adj_list = defaultdict(list)

        for x,y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        while stack:
            current= stack.pop()
            if current == destination:
                return True
            for x in adj_list[current]:
                if x not in seen:
                    seen.add(x)
                    stack.append(x)
        
        return False