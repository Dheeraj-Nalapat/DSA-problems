class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        currentmax ,currentmin = 1,1

        for n in nums:
            temp = currentmax*n
            currentmax = max(currentmax*n,currentmin*n,n)
            currentmin = min(temp,currentmin*n,n)
            res = max(res,currentmax)
        return res    
