class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = list(str(num))
        n.sort()
        a = int(n[0] + n[2])
        b = int(n[1] + n[3])
        return a + b
        