class Solution:
	# @param A : list of integers
	# @param B : list of integers
    def merge(self, A:list, B:list):
        i=0
        j=0
        ans=[]
        while i<len(A) and j<len(B):
            if A[i]>B[j]:
                ans.append(B[j])
                j+=1
            else:
                ans.append(A[i])
                i+=1
            
        while i<len(A):
            ans.append(A[i])
            i+=1
        
        while j<len(B):
            ans.append(B[j])
            j+=1
        
        for _ in range(len(ans)-len(A)):
            A.append(0)
        
        for i in range(len(A)):
            A[i]=ans[i]
        
        return A
    
a=Solution()
a.merge([1,5,8],[3,4])
