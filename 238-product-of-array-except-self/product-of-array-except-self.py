class Solution(object):
    def productExceptSelf(self, nums):
        l_multi = 1
        r_multi = 1
        left_mult = [0] * len(nums)
        right_mult = [0] * len(nums)

        for i in range(len(nums)):
            j = -i-1
            left_mult[i] = l_multi
            right_mult[j] = r_multi
            l_multi *= nums[i]
            r_multi *= nums[j]
            
        
        return [l*r for l, r in zip(left_mult,right_mult)]