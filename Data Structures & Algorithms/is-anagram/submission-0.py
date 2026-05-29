class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=list(s)
        li=list(t)
        l.sort()
        li.sort()
        return l==li
        