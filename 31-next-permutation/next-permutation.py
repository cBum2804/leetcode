class Solution(object):
    def nextPermutation(self, nums):
        last = pointer = len(nums)-1
        while last>0 and nums[last-1]>=nums[last]:
            last-=1
        if last ==0:
            nums.reverse()
            return nums
        incr_pos = last-1
        while nums[pointer]<= nums[incr_pos]:
            pointer-=1
        nums[incr_pos], nums[pointer] = nums[pointer], nums[incr_pos]

        left , right = incr_pos+1, len(nums)-1
        while left< right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1; right-=1
    
        return nums
       