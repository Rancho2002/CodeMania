class Solution:
	# @param A : string
	# @return an integer
    def romanToInt(self, A):
        d={'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM':900,
            'M':1000,
            }
        
        ans=0
        flag=0
        for i in range(len(A)-1):

            if flag==1:
                flag=0
                continue

            if d.get(A[i]+A[i+1]):
                ans=ans+d.get(A[i]+A[i+1])
                flag=1
            else:
                ans=ans+d.get(A[i])
                flag=0
            # print(ans)
        
        if not flag:
            ans=ans+d.get(A[-1])
        
        return ans

a=Solution()
print(a.romanToInt("MMCDLXXV"))