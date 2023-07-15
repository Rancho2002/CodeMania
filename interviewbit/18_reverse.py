import math
class Solution:
	# @param A : integer
	# @return an integer
    def reverse(self, A):
        
        c=1 if A>0 else -1
        A=abs(A)
        i=math.log10(A)
        i=int(i)
        
        
        ans=0
        while A:
            digit=A%10
            ans=ans+digit*pow(10,i) 
            A=A//10
            i-=1
        if ans >= (1<<31): return 0
        return c*ans

a=Solution()
print(a.reverse(1146467285))