class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        temp=x
        while(x!=0):
            if(x<0): x = x*-1
            if(ans<-2147483648/10 or ans>2147483647/10): return 0
            digit=x%10
            ans=ans*10+digit
            x=int(x/10)
        if(temp<0): return ans*-1
        return ans