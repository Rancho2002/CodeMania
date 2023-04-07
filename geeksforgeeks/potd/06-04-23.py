class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equalSum(self,A, N):
        # Your code here
        prefix=[]
        suffix=[]
        left,right=0,0
        for i in A:
            left=left+i
            prefix.append(left)
        for j in A[::-1]:
            right=right+j
            suffix.append(right)
        print(prefix)
        print(suffix)


m=Solution()
a=[1,3,5,2,2]
m.equalSum(a,5)