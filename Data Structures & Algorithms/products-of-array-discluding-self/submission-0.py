class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            m=1
            for j in range(len(nums)):
                if i!=j:
                    m*=nums[j]
            l.append(m)
        return l

        
        