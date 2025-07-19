class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        maxLength = 0
        numSet = set(nums)

        for num in numSet:
            if (num - 1) not in numSet:
                current = num
                count = 1

                while current + 1 in numSet:
                    current += 1
                    count += 1

                maxLength = max(maxLength, count)

        return maxLength
