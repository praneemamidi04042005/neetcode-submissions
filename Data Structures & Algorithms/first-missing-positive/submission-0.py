class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        c=1
        while c in nums:
            c+=1
        return c
        