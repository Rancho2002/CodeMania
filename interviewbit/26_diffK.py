class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    def diffPossible(self, A, B):
        i=0
        j=1
        
        if len(A)==1: return 0
        
        while i < len(A) and j < len(A):
            if A[j]-A[i] == B and i!=j:
                # print(A[j], A[i])
                return 1
            elif A[j]- A[i] < B:
                j+=1
            else:
                i+=1
        return 0
    
a= Solution()
# print(a.diffPossible([ 2, 14, 18, 23, 25, 36, 40, 44, 44, 53, 54, 68, 71, 80, 94 ], 82))
# print(a.diffPossible([ 1,2,3 ], 0))
print(a.diffPossible([ 1, 2, 2, 3, 4 ], 0))