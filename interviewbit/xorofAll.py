class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans=A[0]
        n=len(A)
        if not n&1:
            return 0
        else:
            for i in range(2,n,2):
                ans=ans ^ A[i]
              
            
        
        return ans

a=Solution()
print(a.solve([1,2,3]))