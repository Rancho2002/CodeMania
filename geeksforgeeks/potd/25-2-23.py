'''
class Solution:
    def checkCompressed(self,S, T):
        n = len(S)
        ind = 0
        cur = 0
        
        for i in range(len(T)):
            if T[i] >= 'A' and T[i] <= 'Z':
                ind += cur
                if ind >= n:
                    return 0
                cur = 0
                if S[ind] == T[i]:
                    ind += 1
                else:
                    return 0
            else:
                val = int(T[i])
                cur = cur * 10 + val
        
        if cur > 0:
            ind += cur
        
        return 1 if ind == n else 0
'''


class Solution:
    def checkCompressed(self, S, T):
        # code here 
        j=0
        flag=0
        for i in range(len(T)):
            if(T[i]==S[j]):
                flag=1
                j+=1
            elif(ord(T[i])>=48 and ord(T[i])<=57 and int(T[i])<=len(S)-j):
                j=j*10+int(T[i])
            else:
                flag=0
                break
        
        return 1 if flag else 0
              
var=Solution()
a,b=input(),input()
print(var.checkCompressed(a,b))