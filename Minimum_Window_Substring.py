class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m<n:
            return ""
        l=0
        res= s
        countt={}
        counts={} 
        length = m
        for i in range(n):
            countt[t[i]] = 1+ countt.get(t[i],0)
            counts[t[i]] = 1+ counts.get(t[i],0)
        flag1 = 1    
        for r in range(m):
            if s[r] in countt :
                if s[r] == s[l] and counts.get(s[r],0)-1<0:
                    counts[s[r]] += 1
                    l+=1
                    while(s[l%m] in counts.keys() and counts[s[l%m]]<0):
                            counts[s[l%m]]+=1
                            l+=1
                    while(s[l%m] not in counts.keys()):
                        l+=1
                        while(s[l%m] in counts.keys() and counts[s[l%m]]<0):
                            counts[s[l%m]]+=1
                            l+=1
                counts[s[r]] = counts.get(s[r],0) - 1
                flag=1
                for i in counts.values():
                    if i>0:
                        flag=0
                        break
                if flag:
                    #print(s[l:r+1])
                    flag1=0      
                    temp = length
                    length=min(len(s[l:r+1]),len(res))
                    if len(s[l:r+1])<temp:
                        res = s[l:r+1]
                    counts[s[l]] = 1 + counts.get(s[l],0)
                    l+=1
                    while(s[l%m] in counts.keys() and counts[s[l%m]]<0):
                            counts[s[l%m]]+=1
                            l+=1
                    while(s[l%m] not in counts.keys() and l<m and l>0):
                        l+=1
                        while(s[l%m] in counts.keys() and counts[s[l%m]]<0):
                            counts[s[l%m]]+=1
                            l+=1
                    #print(s[l:r+1])    

            elif l==r:
                l+=1

                
        if flag1:
            res=""
        return res 
