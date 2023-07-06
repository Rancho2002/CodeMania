# https://my.newtonschool.co/playground/code/h66s2xmw0udg
# Your code here
a,b=map(int,input().split())
l=list(map(int,input().split()))

rem= a- sum(l)
if(rem<0):
    print(-1)
else:
    print(rem)