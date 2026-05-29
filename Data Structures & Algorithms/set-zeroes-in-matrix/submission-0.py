class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rm=[]
        cm=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    rm.append(i)
                    cm.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rm or j in cm:
                    matrix[i][j]=0
        
        