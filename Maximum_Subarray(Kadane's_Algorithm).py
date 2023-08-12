def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N==0:
            return 0
        sum_arr = 0
        max_sum = nums[0]
        first = -1
        for i in range(N):
            sum_arr += nums[i]
            if sum_arr>max_sum:
                max_sum = sum_arr
            if sum_arr<0:
                sum_arr=0
        return max_sum 
