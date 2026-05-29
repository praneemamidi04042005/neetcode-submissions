class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i]=='{' or s[i]=='(' or s[i]=='[':
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                else:
                    s1=stack[-1]
                    if s[i]==']' and s1=='[':
                        stack.pop()
                    elif  s[i]=='}' and s1=='{':
                        stack.pop()
                    elif s[i]==')' and s1=='(':
                        stack.pop()
                    else:
                        return False
        return len(stack)==0