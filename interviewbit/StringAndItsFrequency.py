class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        d={}
        for i in A:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        ans=""
        
        for i in d:
            ans= ans+ i+ str(d[i])
        
        
        return ans