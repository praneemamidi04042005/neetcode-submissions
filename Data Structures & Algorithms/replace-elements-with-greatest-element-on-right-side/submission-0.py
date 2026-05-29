class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l=[]
        for i in range(len(arr)):
            m=-1
            for j in range(i+1,len(arr)):
                if arr[j]>m:
                    m=arr[j]
            l.append(m)
        return l
        