class Solution:
    def reverse(self, x: int) -> int:
        n=0
        if x>0:
            while x>0:
                n=(n*10)+(x%10)
                x//=10
            if n>(2**31)-1:
                return 0
            return n
        else:
            x*=-1
            while x>0:
                n=(n*10)+(x%10)
                x//=10
            if -n<(-2**31):
                return 0
            return (-1*n)
