class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l2 = len(matrix)
        r2 = len(matrix[0])
        l1 = 0
        r1 = 0
        res = []
        i,j = 0,0
        flag1,flag2 = 1,0
        while(matrix[i][j]>-100):
            print(matrix[i][j])
            res.append(matrix[i][j])
            matrix[i][j]=-100
            if j>=r1 and j<r2-1 and flag1:
                j+=1
            elif j>r1 and j<=r2-1 and not flag1:
                j-=1
            elif i>=l1 and i<l2-1 and flag1:
                i+=1
            elif i>l1 and i<=l2-1 and not flag1:
                i-=1    
            if i==l2-1 and j==r2-1:
                flag1=0
                l1+=1
            elif i==l1 and j==r1:
                flag1=1
                l2-=1
                r2-=1    
                flag2=1
            elif i==l1 and j==r1+1 and flag2:
                flag2=0
                r1+=1    
            print(i,j,flag1,r1,r2)
        return res   
