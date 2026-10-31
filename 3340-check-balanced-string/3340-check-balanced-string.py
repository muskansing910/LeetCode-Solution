class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        esum=0
        osum=0
        for i in range(len(num)):
            if i%2==0:
                esum+=int(num[i])
            else:
                osum+=int(num[i])
            
        if esum==osum:
            return True
        else:
            return False