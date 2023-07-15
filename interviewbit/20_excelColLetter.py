class Solution:
	# @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        ans=""
        while(A):
            if(A%26==0):
                ch="Z"
            else:
                ch=ord("A")+ (A%26) -1
            
            ch=chr(ch) if ch!="Z" else "Z"
            ans=ch+ans
            A=(A-1)//26
        return ans

a=Solution()
print(a.convertToTitle(943566))
