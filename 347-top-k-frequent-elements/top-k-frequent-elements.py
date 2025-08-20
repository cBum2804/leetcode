class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        result = []
        for key, val in counter.items():
            if len(result)< k:
                heapq.heappush(result, (val,key))
            else:
                heapq.heappushpop(result,(val,key))
        return [h[1] for h in result]
        