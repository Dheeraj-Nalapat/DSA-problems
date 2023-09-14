class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        temp = set(nums)
        nums = list(temp)    
        nums.sort()
        maxstreak,streak=1,1
        for i in range(len(nums)-1):
            if nums[i+1]-1 == nums[i]:
                streak+=1
                if streak>maxstreak:
                    maxstreak=streak
            else:
                streak=1
        return maxstreak 
