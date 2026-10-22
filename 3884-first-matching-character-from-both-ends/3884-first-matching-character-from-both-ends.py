class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i]==s[-(i+1)]:
                return i
                break
        else:
            return -1
