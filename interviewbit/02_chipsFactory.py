class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self,A):
        n = len(A)
        i = 0
        j = 0
        while j < n:
            if A[j] != 0:
                A[i], A[j] = A[j], A[i]
                i += 1
            j += 1
        return A

        
        