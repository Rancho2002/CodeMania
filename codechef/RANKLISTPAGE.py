# https://www.codechef.com/submit/RANKLISTPAGE
# cook your dish here
a=int(input())
for i in range(a):
    b=int(input())
    if(b%25==0):
        print(int(b/25))
    else:
        print(int(b/25)+1)