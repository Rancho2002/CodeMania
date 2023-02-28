# https://www.codechef.com/submit/LOCKDRAW
# cook your dish here
a=int(input())
for i in range(a):
    b,c,d=map(int,input().split())
    if(b+c==d or c+d==b or b+d==c):
        print('YES')
    else:
        print('NO')