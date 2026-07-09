class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        bands=[]
        from bisect import bisect_right
        for i in range(len(startTime)):
            bands.append((startTime[i],endTime[i],profit[i]))
        bands.sort(key=lambda x:x[1])
        dp=[0]*(len(startTime)+1)
        endTimes=sorted(endTime)
        for i in range(1,len(startTime)+1):
            start,end,pop=bands[i-1]
            idx=bisect_right(endTimes,start)-1
            dp[i]=max(dp[i-1],dp[idx+1]+pop)
        return dp[-1]

        