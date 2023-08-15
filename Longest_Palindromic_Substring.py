class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=0
        res = ""
        for l in range(len(s)):
            for r in range(l,len(s)):
                temp = s[l:r+1]
                #print(temp)
                temp1 = temp[::-1]
                #print(temp1)
                if temp == temp1:
                    if len(res)<len(temp):
                        res=temp
        return res  
