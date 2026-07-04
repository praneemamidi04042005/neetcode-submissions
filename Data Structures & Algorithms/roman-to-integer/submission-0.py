class Solution:
    def romanToInt(self, s: str) -> int:
        hm={'I':             1,
        'V'            :5,
        'X'            : 10,
        'L'            : 50,
        'C'             :100,
        'D'          : 500,
        'M'             :1000}
        c=0
        for i in range(len(s)-1):
            if hm[s[i]]<hm[s[i+1]]:
                c-=hm[s[i]]
            else:
                c+=hm[s[i]]
        c+=hm[s[-1]]
        return c



        