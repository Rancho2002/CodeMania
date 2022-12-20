# Your code here
a,b=map(int,input().split())
l=list(map(int,input().split()))

for i in range(41,-1,-1):
    if(((b>>i) & 1 )==1):
        break
req1=0
while(i>=0):
    count=0
    for j in range(a):
        if(((l[j]>>i)&1)==1):
            count+=1
    if(2*count<a):
        if((req1+(1<<i))<=b):
            req1 |=(1 <<i)
    
    i-=1
ans1=0
for j in range(b):
    ans1+=(l[j]^req1)

print(ans1)