class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
		if A<0: return 0
		A=str(A)
		temp=A
		temp=list(temp)
		temp.reverse()
		# print(temp)
		temp=''.join(temp)
		# print(A,temp)
		return 1 if temp==A else 0
	
a=Solution()
print(a.isPalindrome(123))