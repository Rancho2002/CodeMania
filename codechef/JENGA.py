# https://www.codechef.com/submit/JENGA
# cook your dish here
a=int(input())
for i in range(a):
    a,b=map(int,input().split())
    if(a<=b and b%a==0):
        print("YES")
    else:
        print("NO")