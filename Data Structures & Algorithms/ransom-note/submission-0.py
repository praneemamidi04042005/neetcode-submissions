class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm1={}
        for i in ransomNote:
            hm1[i]=hm1.get(i,0)+1
        hm2={}
        for i in magazine:
            hm2[i]=hm2.get(i,0)+1
        for i in hm1:
            if i not in hm2:
                return False
            elif hm2[i]<hm1[i]:
                return False
        return True
        