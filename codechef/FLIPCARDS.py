# https://www.codechef.com/submit/FLIPCARDS
# cook your dish here
a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    if(b-c>=c):
        print(c)
    elif(b==c):
        print(0)
    else:
        print(b-c)