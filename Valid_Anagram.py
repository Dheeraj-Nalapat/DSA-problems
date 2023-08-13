class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for i in s:        
            if i not in t:
                return False
            else:
                t = t[:t.find(i)]+t[t.find(i)+1:]    
        if len(t)==0:
            return True
