class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm={}
        for i in arr:
            hm[i]=hm.get(i,0)+1
        m=-1
        for i in hm:
            if i==hm[i]:
                m=max(i,m)
        return m
        