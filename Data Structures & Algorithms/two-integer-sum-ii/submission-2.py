class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm={}
        l=[]
        i=0
        j=len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]<target:
                i+=1
            elif numbers[i]+numbers[j]>target:
                j-=1
            else:
                l.append(i+1)
                l.append(j+1)
                break
        return l