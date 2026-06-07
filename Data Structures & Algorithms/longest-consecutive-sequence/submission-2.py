class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        if not nums:
            return 0
        m=0
        c=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                c+=1
            else:
                m=max(c,m)
                c=1
        m=max(c,m)
        return m
        