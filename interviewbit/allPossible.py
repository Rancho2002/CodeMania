class Solution:
    # @param A : list of strings
    # @return a list of strings
    def specialStrings(self, A):
        ans=[]
        for i in range(len(A)-1):
            for j in range(len(A[i])):
                for k in range(1,len(A)):
                    for l in range(len(A[k])):
                        ans.append(A[i][j]+A[k][l])
        
        return ans


a=Solution()
# print(a.specialStrings(['aa', 'bb']))

# print(a.specialStrings(['ab', 'cd']))
print(a.specialStrings([ "ozqz", "p", "abm" ]))