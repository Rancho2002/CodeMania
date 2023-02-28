# https://www.codechef.com/submit/NONNEGPROD
# cook your dish here
a=int(input())
m=1
count=0
for i in range(a):
    int(input())
    l=list(map(int,input().split()))
    for j in range(len(l)):
        m=m*l[j]
        if(l[j]<0):
            count+=1
    if(m<0):
        print(count)
    else:
        print(0)