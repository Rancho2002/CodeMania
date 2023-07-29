class Solution:
	# @param A : integer
	# @return an integer

    #ans= A/5 + A/25 + A/125 + ....
    def trailingZeroes(self, A):
        x=5
        c=0
        while(x<=A):
            c+= A//x
            x=x*5
        return c

a=Solution()
print(a.trailingZeroes(5))