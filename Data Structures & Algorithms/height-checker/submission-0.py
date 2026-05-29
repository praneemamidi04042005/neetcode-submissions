class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l=heights[:]
        l.sort()
        c=0
        for i in range(len(heights)):
            if l[i]!=heights[i]:
                c+=1
        return c