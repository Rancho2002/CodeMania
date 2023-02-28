# Your code here
n=int(input())
l={}

for i in range(n):
    s=input()
    m="".join(sorted(s))
    if(m in l):
        l[m]=l[m]+1
    else:
        l[m]=1
count=0
for i in l:
    if(l[i]>1):
        count+=(l[i]*(l[i]-1))/2
print(int(count))