class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for l in range(len(s)):
            for r in range(l,len(s)):
                temp = s[l:r+1]
                temp1 = temp[::-1]
                if temp == temp1:
                    count+=1
        return count
