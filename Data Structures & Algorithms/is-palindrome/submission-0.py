class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ss=''
        for i in s:
            if ord(i) in range(97,123):
                ss+=i
            elif ord(i) in range(65,91):
                ss+=i
            elif ord(i) in range(48,58):
                ss+=i
        return ss==ss[::-1]
        