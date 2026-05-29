class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=[]
        for i in range(len(temperatures)):
            l.append(0)
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    l[i]=j-i
                    break
        return l
        