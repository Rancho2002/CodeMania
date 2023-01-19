# Your code here
n,m=map(int,input().split())
chk=0
for i in range(n+1,m):
    if(i%2==0 and chk!=5):
        print(i,end=" ")
        chk+=1
# end of program