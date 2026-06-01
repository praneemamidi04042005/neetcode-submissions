class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def generateRow(row):
            ansRow=[]
            ans=1
            ansRow.append(ans)
            for col in range(1,row):
                ans*=(row-col)
                ans//=col
                ansRow.append(ans)
            return ansRow
        res=[]
        for i in range(1,numRows+1):
            res.append(generateRow(i))
        return res
        