class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        subString = []
        maxLength = 0
        left = 0
        for right in range(len(s)):
            
            while s[right] in subString:
                 subString.remove(s[left])
                 left += 1

            subString.append(s[right])
            maxLength = max(max, right - left + 1)

        return maxLength