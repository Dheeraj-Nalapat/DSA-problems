class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        test = s[0]
        res=[]
        for i in range(len(s)):
            if s[i] in test:
                res.append(test)
                test = test[(test.find(s[i])+1):]
                test = test+s[i]
            elif  i == len(s)-1:
                test = test + s[i]
                res.append(test)    
            else :
                test = test + s[i]
        large = 0     
        for i in range(len(res)):
            if len(res[i]) > large:
                large = len(res[i])
        return large 
