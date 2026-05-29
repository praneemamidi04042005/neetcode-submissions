class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=[]
        for i in nums:
            if i!=val:
                l.append(i)
        for i in range(len(nums)-nums.count(val)):
            nums[i]=l[i]
        return len(l)        