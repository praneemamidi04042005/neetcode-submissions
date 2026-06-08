class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        for i in range(len(s)):
            p=[]
            for j in range(i,len(s)):
                if s[j] in p:
                    break
                else:
                    p.append(s[j])
                    m=max(m,j-i+1)
        return m
        