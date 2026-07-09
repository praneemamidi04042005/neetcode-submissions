class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails=[]
        from bisect import bisect_left
        for i in nums:
            pos=bisect_left(tails,i)
            if pos==len(tails):
                tails.append(i)
            else:
                tails[pos]=i
        return len(tails)
        