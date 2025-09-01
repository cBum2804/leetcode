class Solution(object):
    def findItinerary(self, tickets):
        stack = []
        adj_list = defaultdict(list)
        result = []
        for src, dst in tickets:
            heapq.heappush(adj_list[src], dst)
        
        stack.append("JFK")
        
        while stack:
            while adj_list[stack[-1]]:   
                next_dst = heapq.heappop(adj_list[stack[-1]])
                stack.append(next_dst)
            result.append(stack.pop())   

        return result[::-1]
        
        