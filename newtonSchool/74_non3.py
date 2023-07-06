# Your code here
count=0
i=1
n=int(input())
while(i):
    if(i%3!=0 and i%10!=3):
        count+=1
    if(count==n):
        print(i)
        break
    i+=1