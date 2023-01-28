# Your code here
sum=(lambda x,y:x+y)
l=list(map(int,input().split()))
flag=False
for i in range(len(l)-1):
    if(sum(l[i],l[i+1])%2==0 and sum(l[i],l[i+1])>0):
        flag=True
        break
print("YES" if flag else "NO")