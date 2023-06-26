class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substr = ""
        length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] in substr:
                index = substr.index(s[i])
              #string Slicing has been used
                substr = substr[index + 1:]
                length = len(substr)
            substr += s[i]
            length += 1
            max_length = max(max_length, length)
        return max_length
