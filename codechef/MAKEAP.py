# Contest Link: https://www.codechef.com/START68D/problems/MAKEAP
for i in range(int(input())):
    a,b=map(int,input().split())
    c=(b+a)
    if(c%2!=0):
        print(-1)
    else:
        print(int(c/2))