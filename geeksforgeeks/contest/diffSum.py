class Solution:
    def diffSum(self, n, m, arr): 
        # code here 
        arr.sort()
        set1=arr[0:m]
        set2=arr[-m:]
        print(set1,set2)
        return abs(sum(set1)-sum(set2))

a=Solution()
a.diffSum(5,4,[1,2,3,4,5])