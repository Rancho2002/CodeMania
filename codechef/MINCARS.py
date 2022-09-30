# https://www.codechef.com/submit/MINCARS
# cook your dish here
a=int(input())
for i in range(a):
    b=int(input())
    if(b%4==0):
        print(int(b/4))
    else:
        print(int(b/4)+1)