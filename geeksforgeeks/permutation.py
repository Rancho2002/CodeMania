# #User function Template for python3
# def factorial(n:int)->int:
#     p=1
#     for i in range(1,n+1):
#         p=p*i
#     return p
    
# class Solution:
#     def find_permutation(self, S):
#         # Code here
#         d={}
#         for i in S:
#             if(i in d):
#                 d[i]+=1
#             else:
#                 d[i]=1
        
#         key=list(d.keys())
#         val=list(d.values())
        
#         ans=factorial(len(key))
#         for i in val:
#             if(i>1):
#                 ans=ans//factorial(i)
#         return ans
from itertools import permutations
    
class Solution:
    def find_permutation(self, S):
        # Code here
        ans=permutations(S,len(S))
        l=[]
        for i in ans:
            l.append("".join(i))
        return l

a=Solution()
print(a.find_permutation("ABD"))