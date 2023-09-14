class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        child = ratings
        inc = [1]*n
        total=0
        j=0
        for i in range(1,n):
            if child[i-1]<child[i]:
                inc[i]=inc[i-1]+1
        for i in range(n-1,0,-1):
            if child[i]<child[i-1] and inc[i]>=inc[i-1]:
                inc[i-1]=inc[i]+1
        total = sum(inc)        
        return total   
