class Solution(object):
    def sumCounts(self, nums):

        a = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                a+=len(set(nums[i:j]))**2

        return a