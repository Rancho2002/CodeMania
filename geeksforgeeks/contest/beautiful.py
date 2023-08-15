class Solution:
    
    def digiSq(self,n):
        ans=0
        while n:
            digi=n%10
            ans=ans+digi**2
            n=n//10
        return ans 
          
    def beautifulNumber(self, n : int) -> bool:
        # code here
        track={}
        temp=n
        while track.get(temp)!=1:
            track[temp]=1
            temp=self.digiSq(temp)
            if temp==1:
                return True
        
        return False
        
    
a=Solution()
print(a.beautifulNumber(19))
        