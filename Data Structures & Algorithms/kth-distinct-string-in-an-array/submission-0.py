class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hm={}
        for i in arr:
            hm[i]=hm.get(i,0)+1
        l=[]
        for i in arr:
            if hm[i]==1:
                l.append(i)
        if k-1 in range(len(l)):
            return l[k-1]
        else:
            return ""

        