# https://www.codechef.com/submit/FINDSHOES
a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    req=b*2
    if(c>b):
        c=b
        need=req-c
    else:
        need=req-c
    print(need)