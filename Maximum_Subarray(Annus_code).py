def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = nums[0]
        largest = nums[0]
        l = nums[1:]
        for x in l:
            sum+=x
            sum = max(x,sum)
            largest = max(largest,sum)
            print(largest)
        return largest
