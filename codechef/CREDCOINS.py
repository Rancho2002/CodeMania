# https://www.codechef.com/submit/CREDCOINS
# cook your dish here
a=int(input())
for i in range(a):
    a,b=map(int,input().split())
    c=a*b
    print(c//100)