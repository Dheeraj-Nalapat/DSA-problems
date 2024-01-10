class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        index = len(digits)-1
        while(carry and index!=-1):
            digits[index] += 1
            carry = digits[index]//10
            digits[index] %= 10
            index-=1
        if carry:
            return [1]+digits
        else:
            return digits        
