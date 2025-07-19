class Solution(object):
    def lengthOfLongestSubstring(self, s):
       left = maxLength = 0;
       charSet = set()

       for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)

       return maxLength

        