class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l=nums[:]
        l.sort()
        p=nums[:]
        p.sort(reverse=True)
        if p==nums or l==nums:
            return True
        else:
            return False
        