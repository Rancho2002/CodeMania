# https://www.codechef.com/problems/TRICOIN
# cook your dish here
def isPossible(m:int,n:int)->bool:
    if((m*(m+1))//2 )<=n:
        return True
    return False


n=int(input())
for i in range(n):
    s=0
    tmp=int(input())
    e=tmp
    ans=-1
    m=s+(e-s)//2
    while(s<=e):
        if(isPossible(m,tmp)):
            ans=m
            s=m+1
        else:
            e=m-1
        m=s+(e-s)//2
    print(ans)
    