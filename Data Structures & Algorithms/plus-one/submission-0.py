class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s+=str(i)
        l=int(s)+1
        p=[]
        while l>0:
            p.append(l%10)
            l//=10
        return p[::-1]
        