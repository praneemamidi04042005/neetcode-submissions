class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        return list(bin(n)[2::]).count('1')
        