# Your code here
a,b,c=map(int,input().split())
count=0
while(b>a):
    a=a*c
    count+=1
print(count)