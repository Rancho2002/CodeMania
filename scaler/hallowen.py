from math import ceil
class Solution:
    # @param A : integer
     # @return an long
    def solve(self, A):
        ans=0
        for i in range(A,-1,-1):
            n=i
            x=i
            while n>0:
                ans=ans+x
                x=x-ceil(x/2)
                n=n//2
        return ans

a=Solution()
print(a.solve(8))


