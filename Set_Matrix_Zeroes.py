class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=[]
        c=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    r.append(i)
                    c.append(j)
        temp = set(r)
        #r = list(temp)
        for i in temp:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        temp = set(c)
        #c = list(temp)
        for i in range(len(matrix)):
            for j in temp:
                matrix[i][j]=0
