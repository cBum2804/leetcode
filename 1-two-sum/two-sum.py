class Solution(object):
    def twoSum(self, nums, target):
        mapper =  {val: idx for idx, val in enumerate(nums) }

        for i in range(len(nums)):
            if target-nums[i] in mapper and mapper[target-nums[i]]!= i:
                return i, mapper[target-nums[i]]  
        return 0