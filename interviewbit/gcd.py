class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
    def gcd(self, A, B):
        if B==0:
            return A
        if A==0:
            return B
            
        if A>B:
            return self.gcd(A%B,B)
        else:
            return self.gcd(A,B%A)

a=Solution()
print(a.gcd(4,6))