class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(32):
            if(pow(2,i)==n): return True
        return False