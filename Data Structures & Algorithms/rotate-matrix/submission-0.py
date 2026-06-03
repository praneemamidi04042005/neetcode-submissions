class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        k=[]
        for j in range(m):
            p=[]
            for i in range(m):
                p.append(matrix[i][j])
            k.append(p)
        for i in range(m):
            k[i]=k[i][::-1]
        for i in range(m):
            matrix[i]=k[i]

        