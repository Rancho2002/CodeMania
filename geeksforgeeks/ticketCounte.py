class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        # Code Here
        x=[i for i in range(1,N+1)]
        
        f=0
        b=0

        for _ in range(N):
            if(x and f!=K and b==0):
                r=x.pop(0)
                f+=1

            if(f==K and b==0):
                b=K
            if(x and b!=0 and f==K):
                r=x.pop()
                b-=1
            
            if(b==0 and f==K):
                f=0


        return r
        
        '''
        1 2 3 4 5 6 7 8 9 10 11 12 13 14
        10 11 12 13 14
        '''


a=Solution()
print(a.distributeTicket(5,1))