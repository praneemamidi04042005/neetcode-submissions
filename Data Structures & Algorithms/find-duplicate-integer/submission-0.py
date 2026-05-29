class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m=dict()
        for i in nums:
            m[i]=m.get(i,0)+1
            if m[i]>1:
                return i