n=int(input())
d={}

for i in range(n):
    d[i]=max(list(map(int, input().split())))

s,e=map(int, input().split())
ans=0
curr=s

while curr!=e and ans<n:
    curr=d[s-1]
    s=curr
    ans+=1

if curr!=e:
    print(ans)
else:
    print(-1)