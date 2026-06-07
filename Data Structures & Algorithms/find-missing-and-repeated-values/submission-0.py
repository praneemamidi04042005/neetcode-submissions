class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)*len(grid)
        hm={}
        for i in range(len(grid)):
            for j in range(len(grid)):
                hm[grid[i][j]]=hm.get(grid[i][j],0)+1
        l=[]
        for i in hm:
            if hm[i]>1:
                l.append(i)
        for i in range(1,n+1):
            if i not in hm:
                l.append(i)
        return l