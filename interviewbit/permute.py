from itertools import permutations

class Solution:
	# @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        s=""
        for i in A:
            s+=str(i)
        ans=permutations(s)
        return list(ans)

a=Solution()
print(a.permute([1,2,3]))