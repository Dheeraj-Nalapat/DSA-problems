class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num = x
        rev = 0
        while  num>0:
            rev *=10
            temp = num%10
            num = num//10
            rev += temp
        if rev == x:
            return True
        else:
            return False 
