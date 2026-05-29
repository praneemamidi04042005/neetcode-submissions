class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm={}
        l=[]
        for i in nums:
            hm[i]=hm.get(i,0)+1
        for i in hm:
            if hm[i]>math.floor(len(nums)/3):
                l.append(i)
        return l
        