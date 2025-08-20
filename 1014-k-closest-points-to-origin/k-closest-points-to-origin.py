class Solution(object):
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            if len(heap)< k:
                heapq.heappush(heap, (-(x**2 + y**2),x,y))
            else:
                heapq.heappushpop(heap,(-(x**2 +y**2),x,y))
        
        return [(x,y) for d,x,y in heap]


        