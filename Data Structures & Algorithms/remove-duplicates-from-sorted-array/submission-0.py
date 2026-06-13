class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hm={}
        for i in nums:
            hm[i]=hm.get(i,0)+1
        l=[]
        for i in hm:
            l.append(i)
        for i in range(len(l)):
            nums[i]=l[i]
        return len(l)