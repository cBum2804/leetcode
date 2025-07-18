class Solution(object):
    def searchRange(self, nums, target):
        def binary_search(nums, target, is_right):
            left = 0;
            right = len(nums)-1
            index = -1;

            while left<=right:
                mid = (left+right)/2

                if nums[mid]< target:
                    left = mid +1
                elif nums[mid]> target:
                    right = mid-1;
                else:
                    index = mid
                    if is_right:
                        left = mid+1
                    else:
                        right = mid-1

            return index
        right = binary_search(nums, target, True)
        left = binary_search(nums, target, False)

        return[left, right]
        