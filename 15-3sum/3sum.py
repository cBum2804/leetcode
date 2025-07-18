class Solution(object):
    def threeSum(self, nums):
        targetSum = 0;
        nums.sort()
        numSet = set()
        output = []

        for i in range(len(nums)):
            m = i+1
            n = len(nums)-1
            while m<n:
                sum = nums[i] + nums[m] + nums[n];
                if sum == targetSum:
                    numSet.add((nums[i], nums[m], nums[n]))
                    m+=1
                    n-=1
                elif sum < targetSum:
                    m+=1
                else:
                    n-=1
        ans = list(numSet)
        return ans

        
        