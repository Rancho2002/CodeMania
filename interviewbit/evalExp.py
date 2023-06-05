class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
            l=["+","-","/","*"]
            m=[]
            for i in range(len(A)):
                # print(A[i])
                if A[i] not in l:
                    m.append(A[i])
                    # print(m)
                else:
                    # print(m,i)

                    op1=int(m[len(m)-1])
                    op2=int(m[len(m)-2])
                    if(A[i]=="+"):
                        ans=op1+op2
                    elif(A[i]=="*"):
                        ans=op1*op2
                    elif(A[i]=="-"):
                        ans=op2-op1
                    elif(A[i]=="/"):
                        ans=op2//op1
                    m.pop()
                    m.pop()
                    m.append(ans)
            return m[0]

a=Solution()
print(a.evalRPN(["4", "13", "5", "/", "+"]))
                    