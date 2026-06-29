class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        for i in operations:
            if i=='+':
                p1=st[-1]
                p2=st[-2]
                st.append(p1+p2)        
            elif i=='D':
                p1=st[-1]
                st.append(p1*2)        
            elif i=='C':
                st.pop()
            else:
                st.append(int(i))
        return sum(st)        