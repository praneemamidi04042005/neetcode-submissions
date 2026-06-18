class Solution:
    def isSafe(self,row,col,board,n):
        for j in range(col):
            if board[row][j]=="Q":
                return False
        i=row
        j=col
        while i>=0 and j>=0:
            if board[i][j]=="Q":
                return False
            i-=1
            j-=1
        
        i=row
        j=col
        while i<n and j>=0:
            if board[i][j]=="Q":
                return False
            i+=1
            j-=1
        return True
    def solve(self,col,ans,board,n):
        if col==n:
            temp=[''.join(row) for row in board]
            ans.append(temp)
            return 
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row][col]="Q"
                self.solve(col+1,ans,board,n)
                board[row][col]="."
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.' for i in range(n)]for i in range(n)]
        ans=[]
        self.solve(0,ans,board,n)
        return ans
        