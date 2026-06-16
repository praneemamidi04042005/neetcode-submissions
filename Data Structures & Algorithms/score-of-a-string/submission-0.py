class Solution:
    def scoreOfString(self, s: str) -> int:
        hm={}
        sc=0
        for i in range(97,123):
            hm[chr(i)]=i
        for i in range(1,len(s)):
            sc+=abs(hm[s[i]]-hm[s[i-1]])
        return sc
        