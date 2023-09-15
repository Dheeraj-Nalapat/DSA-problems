class Solution:
    def trap(self, height: List[int]) -> int:
        maxl,maxr=height[0],height[len(height)-1]
        l,r=0,len(height)-1
        total=0
        while l<r:
            if maxl<maxr:
                l+=1
                if maxl<height[l]:
                    maxl=height[l]
                else:
                    total+= maxl-height[l]
            else:
                r-=1
                if maxr<height[r]:
                    maxr=height[r]
                else:
                    total+= maxr-height[r]        
        return total  
