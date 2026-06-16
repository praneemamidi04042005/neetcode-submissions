class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm={}
        hm2={}
        for i in range(len(s)):
            if s[i] not in hm:
                hm[s[i]]=t[i]
            elif s[i] in hm and hm[s[i]]!=t[i]:
                return False
        for i in range(len(s)):
            if t[i] not in hm2:
                hm2[t[i]]=s[i]
            elif t[i] in hm and hm2[t[i]]!=s[i]:
                return False
        return True
        