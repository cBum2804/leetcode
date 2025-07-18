class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        min_diff = float('inf')

        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1

            while(left < right):
                curr_sum = nums[i] + nums[left] + nums[right]
                curr_diff = abs(curr_sum - target)

                if curr_diff < min_diff:
                    min_diff = curr_diff;
                    closest_sum = curr_sum
                
                if curr_sum< target:
                    left+=1
                else:
                    right-=1
        return closest_sum