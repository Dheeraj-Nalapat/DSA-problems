class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        l,r=0,0
        temp = 0
        contemp = 0
        prevmax=0
        revheight = height[::-1]
        for r in range(len(height)):
            if height[r]>=prevmax:
                while(l!=r):
                    print(count)
                    print(prevmax)
                    count+=(prevmax-height[l])
                    l+=1
                prevmax = height[r]
        l,prevmax=0,0        
        for r in range(len(revheight)):    
            if revheight[r]>prevmax:
                while(l!=r):
                    print(count)
                    print(prevmax)
                    count+=(prevmax-revheight[l])
                    l+=1
                prevmax = revheight[r]    
        return count
