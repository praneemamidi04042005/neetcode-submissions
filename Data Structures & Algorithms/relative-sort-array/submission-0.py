class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        hm={}
        for i in arr1:
            hm[i]=hm.get(i,0)+1
        for i in arr2:
            for j in range(hm[i]):
                l.append(i)
        k=[]
        for i in arr1:
            if i not in arr2:
                k.append(i)

        k.sort()
        l.extend(k)
        return l
        