class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        front= [1]
        for i in range(len(nums)-1):
            front.append(front[i]*nums[i])
        back = [1]
        n = len(nums)
        for i in range(len(nums)-1):
            back.append(back[i]*nums[n-i-1])
        answer = []
        for i in range(n):
            answer.append(back[n-i-1]*front[i])
        return answer            
