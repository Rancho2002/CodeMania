# Your code here
a,b=map(int,input().split())
c=""
while(a):
    c+=str(a%b)
    a=a//b
print(len(c))