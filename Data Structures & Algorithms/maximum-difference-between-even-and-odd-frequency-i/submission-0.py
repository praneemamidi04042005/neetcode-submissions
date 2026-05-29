class Solution:
    def maxDifference(self, s: str) -> int:
        
        hm={}
        for i in s:
            hm[i]=hm.get(i,0)+1
        ef=[]
        of=[]
        for i in hm:
            if hm[i]%2==0:
                ef.append(hm[i])
            else:
                of.append(hm[i])
        return max(of)-min(ef)