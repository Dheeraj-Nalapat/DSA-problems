class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow , fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow2 == slow:
                return slow
