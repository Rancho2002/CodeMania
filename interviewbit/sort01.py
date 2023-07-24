class Solution:
    # @param A : list of integers
    # @return a list of integers
    def swap(self,A,i,j):
        A[i],A[j]=A[j],A[i]
        
    def solve(self, A):
        i=0
        j=len(A)-1
        while(i<=j):
            if A[i]==1 and A[j]==0:
                self.swap(A,i,j)
                j-=1
                i+=1
            
            elif A[i]==0:
                i+=1
            
            elif A[i]==1:
                j-=1
                
        return A