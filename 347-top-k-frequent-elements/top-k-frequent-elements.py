class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        mapper = [0]* (len(nums)+1)
        result = []
        for key, freq in counter.items():
            if mapper[freq]==0:
                mapper[freq] = [key]
            else:
                mapper[freq].append(key)
        
        for i in range(len(nums),-1,-1):
            if mapper[i]!=0:
                result.extend(mapper[i])
            if len(result)==k:
                break
        return result