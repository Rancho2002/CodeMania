class Solution:
    def solve(self,N,S):
        #code here
        arr=[0]*26
        for i in S:
            arr[ord(i)-ord("a")]+=1
        print(arr)
        maxi=arr[0]
        ans=0
        for i in range(26):
            if arr[i]>maxi:
                ans=i
                maxi=arr[i]
                
        return chr(97+ans)

a=Solution()
a.solve(6,"gfgfgf")