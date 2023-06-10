class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 1
        for i in range(len(A)-1, -1, -1):
            if A[i] + carry == 10:
                A[i] = 0
                carry = 1
            else:
                A[i] = A[i] + carry
                carry = 0
        
        if A[0] + carry == 10:
            A[0] = 0
            A.insert(0, 1)
        else:
            A[0] = A[0] + carry
        
        while A[0] == 0:
            A.remove(A[0])
        
        return A
