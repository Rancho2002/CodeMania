class Solution:
    # @param A : string
    # @return a list of strings
    def deserialize(self, A):
        
        temp=""
        ans=[]

        for i in A:
            if i=="~":
                ans.append(temp)
                temp=""
            else:
                temp+=i

        for i in range(len(ans)):
            for j in range(len(ans[i])-1,-1,-1):
                if ans[i][j].isalpha():
                   break

            ans[i]=ans[i][0:j+1]

        return ans

a=Solution()
print(a.deserialize("interviewbit12~"))
# print(a.deserialize("scaler6~academy7~"))``