# cook your dish here
a=int(input())
for i in range(a):
    a,b,c=map(int,input().split())
    if((a+b)/2 >c):
        print("YES")
    else:
        print("NO")