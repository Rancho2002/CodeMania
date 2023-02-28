# Your code here
n=int(input())
l=list(map(int,input().split()))
count=0
for i in l:
    if i >10:
        count+=i-10
print(count)