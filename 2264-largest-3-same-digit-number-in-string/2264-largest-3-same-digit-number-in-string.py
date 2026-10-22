class Solution(object):
    def largestGoodInteger(self, nums):
        """
        :type num: str
        :rtype: str
        """
        prev=''
        for i in range(len(nums)):
            if nums[i]==nums[i-1] and nums[i]==nums[i-2]:
                if nums[i]>prev:
                    prev=nums[i]
        return prev*3


