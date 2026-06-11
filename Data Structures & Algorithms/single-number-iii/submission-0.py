class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l=[]
        hm={}
        for i in nums:
            hm[i]=hm.get(i,0)+1
        for i in hm:
            if hm[i]==1:
                l.append(i)
        return l
        