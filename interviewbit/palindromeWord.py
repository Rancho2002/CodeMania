def palindrome(a: str) -> bool:
    mid = len(a) // 2
    for i in range(mid):
        if a[i] != a[len(a) - 1 - i]:
            return False
    return True

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        ans=0
        variables=A.split(" ")
        for i in variables:
            if(palindrome(i)):
                ans+=1
        return ans
                

a=Solution()
print(a.solve("wow mom"))