class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=list(s1)
        l.sort()
        for i in range(len(s2)-len(s1)+1):
            k=list(s2[i:i+len(s1)])
            k.sort()
            
            if k==l:
                return True
        return False
        