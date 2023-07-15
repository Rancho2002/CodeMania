class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
		ans = 0
		n = len(A)

		for i in range(n-1, -1, -1):
			ans += pow(26, n-1-i) * (ord(A[i]) - ord('A') + 1)

		return ans


a=Solution()
print(a.titleToNumber("AA"))