class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l=[]
        for i in queries:
            c=0
            for j in range(i[0],i[1]+1):
                if words[j][-1] in 'aeiou' and words[j][0] in 'aeiou':
                    c+=1
            l.append(c)
        return l