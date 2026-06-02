class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1=0
        maxi=float('-inf')
        i=0
        while i<len(nums):
            if sum1<0:
                sum1=0
            sum1+=nums[i]
            maxi=max(sum1,maxi)
            i+=1
        return maxi
        