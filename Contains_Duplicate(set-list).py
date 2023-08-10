class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        temp = set(nums)
        m = len(temp)
        print(n)
        print(m)
        if n!=m:
            return True
        elif n==m:
            return False         
