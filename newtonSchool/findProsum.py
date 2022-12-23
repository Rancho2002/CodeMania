# Your code here
n=int(input())
l=list(map(int,input().split()))
tosum=l[n-1]
ans=0
mod=10**9+7

for i in range(n-2,-1,-1):
    ans=(ans+(tosum*l[i]))
    tosum=(tosum+l[i])


print(ans%mod)
