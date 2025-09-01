class Solution(object):
    def findItinerary(self, tickets):
        stack = []
        adj_list = defaultdict(list)
        result = []
        for src, dst in tickets:
            heapq.heappush(adj_list[src], dst)
        
        stack.append("JFK")
        
        while stack:
            curr = stack.pop()  
            while adj_list[curr]:
                next_dst = heapq.heappop(adj_list[curr])
                stack.append(curr)     
                stack.append(next_dst) 
                break                  
            else:
                
                result.append(curr)

        return result[::-1]
        
        