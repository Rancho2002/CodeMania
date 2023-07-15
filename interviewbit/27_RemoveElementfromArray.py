class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        j=0
        i=0       
        while(i<len(A)):
            if A[i]!=B:
                A[i],A[j]=A[j],A[i]
                j+=1
            i+=1
            
        return j
    