class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2:
            return 0
        nums.sort()
        if len(nums)==2 :
            return nums[1]-nums[0]
        maxDiff = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i]> maxDiff:
                maxDiff = nums[i+1]-nums[i]
        return maxDiff