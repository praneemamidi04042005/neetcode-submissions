class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l=[]
        for i in range(len(matrix[0])):
            p=[]
            for j in range(len(matrix)):
                p.append(matrix[j][i])
            l.append(p)
        return l
        