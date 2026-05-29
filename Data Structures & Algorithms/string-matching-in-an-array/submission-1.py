class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l=[]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[j] in words[i]:
                    l.append(words[j])
                elif words[i] in words[j]:
                    l.append(words[i])
        return list(set(l))
        