# Your code here
a,b,k=map(int,input().split())
if(k-a>=0):
    if(b-(k-a)<0):
        print(0,0)
    else:
        print(0,b-(k-a))
else:
    print(a-k,b)