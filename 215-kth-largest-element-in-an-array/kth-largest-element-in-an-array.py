class Solution(object):
    def findKthLargest(self, nums, k):
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        count = k
        while count > 1:
            heapq.heappop(nums)
            count-=1
        return -heapq.heappop(nums)
        