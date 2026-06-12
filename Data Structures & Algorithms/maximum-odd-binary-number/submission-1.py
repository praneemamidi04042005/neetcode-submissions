class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ss='1'
        hm={}
        for i in s:
            hm[i]=hm.get(i,0)+1
        if '0' in hm:
            for i in range(hm['0']):
                ss='0'+ss
        if '1' in hm:
            for i in range(hm['1']-1):
                ss='1'+ss
        return ss