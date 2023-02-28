class Solution:
    def hammingWeight(self, n: int) -> int:
       n=str(bin(n))
       n=list(n.strip())
       return n.count("1")