class Solution:
	# @param A : integer
	# @return an integer
	def isPrime(self, A):
            if A==1: return 0
            count=0
            for i in range(1,int(A**0.5)+1):
                if(A%i==0):
                    count+=1
            return 1 if count==1 else 0
            