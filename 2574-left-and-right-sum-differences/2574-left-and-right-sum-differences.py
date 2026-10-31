class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li=[]
        for i in range(len(nums)):
            l=0
            r=0
            res=0
            for j in range(len(nums)):
                if i<j:
                    r+=nums[j]
                elif i>j:
                    l+=nums[j]

                res=abs(l-r)
            li.append(res)
        return li