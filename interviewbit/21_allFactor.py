class Solution:
	# @param A : integer
	# @return a list of integers
	def allFactors(self, A):
		l=[]
		for i in range(1,int(A**0.5)+1):
			if(not A%i):	
				l.append(i)
		if A!=1: l.append(A)
		return l
a=Solution()
print(a.allFactors(1))