class Solution:
	# @param A : tuple of integers
	# @return an integer
    def maxProfit(self, A):
        if(len(A)==0): return 0
        high=max(A)
        low=min(A)
        while(A.index(high) < A.index(low) and len(A)>=2):
            A.pop(A.index(high))
            high=max(A)
            low=min(A)
        if(A.index(high)>A.index(low)):
            return high-low
        return 0

a=Solution()
print(a.maxProfit([1, 2]))