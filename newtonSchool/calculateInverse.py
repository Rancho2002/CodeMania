n=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(n):
    ans+=(1/l[i])

ans=1/ans

print(f"{ans:.8f}")