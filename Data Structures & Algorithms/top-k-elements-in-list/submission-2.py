class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for i in nums:
            hm[i]=hm.get(i,0)+1
        l=[]
        for i in hm:
            l.append((hm[i],i))
        l.sort(reverse=True)
        p=[]
        for i in range(k):
            p.append(l[i][1])
        return p

        