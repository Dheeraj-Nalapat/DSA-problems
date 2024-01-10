class Solution:
    def isHappy(self, n: int) -> bool:
        listNumbers = []
        while(n!=1):
            if n in listNumbers:
                break
            else:
                listNumbers.append(n)
            sumSquare = 0
            while(n):
                digit = n%10
                sumSquare += digit*digit
                n = n//10
            n = sumSquare
                
            if n==1:
                print(listNumbers)
                return True
        return True if n==1 else False     
