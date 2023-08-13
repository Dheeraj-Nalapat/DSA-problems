class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=""
        for i in s.split(" "):
            strs += i.lower()
        i=0    
        print(strs)
        while(i!=len(strs)):
            if (strs[i].isalnum()):
                i+=1
            else:
                strs = strs[:i]+strs[i+1:]

        print(strs)    
        temp = strs[::-1]
        if temp == strs:
            return True
        else:
            return False  
