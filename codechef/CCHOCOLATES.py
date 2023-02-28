# cook your dish here
a=int(input())
for i in range(a):
    a,b,c=map(int,input().split())
    print(int((a*5+b*10)/c))