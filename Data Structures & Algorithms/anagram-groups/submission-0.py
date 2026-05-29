class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for i in strs:
            l=list(i)
            l.sort()
            s=''.join(l)
            if s not in hm:
                hm[s]=[]
            hm[s].append(i)
        p=[]
        for i in hm:
            p.append(hm[i])
        return p
        