class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            if nums.count(nums[i])>1:
                l.append(nums[i])
                break
        for i in range(1,len(nums)+1):
            if i not in nums:
                l.append(i)
                break
        return l
        