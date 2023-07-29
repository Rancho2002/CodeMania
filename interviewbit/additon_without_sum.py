class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def addNumbers(self, A, B):
        while(B):
            c=A&B
            print(c,A,B)
            A=A^B
            B=c<<1
        return A

a=Solution()
print(a.addNumbers(4,5))