from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm=defaultdict(int)
        i=0
        res=0
        for j in range(len(s)):
            hm[s[j]]+=1
            maxfreq=max(hm.values())
            curlen=j-i+1
            if curlen-maxfreq>k:
                hm[s[i]]-=1
                i+=1
            res=max(res,j-i+1)
        return res
        