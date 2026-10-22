class Solution(object):
    def trafficSignal(self, timer):
        """
        :type timer: int
        :rtype: str
        """
        s=''
        if timer == 0:
            s+="Green"
        elif timer==30:
            s+="Orange"
        elif timer>=30 and timer<=90:
            s+="Red"
        else:
            s+="Invalid"
        return s