a,b=map(int,input().split())
l=list(map(int,input().split()))

d={}
sum=0
for i in range(b):
    d[i]=i

# print(d)

for j in d:
    for i in l:
        sum+=d[j]^i
    d[j]=sum
    sum=0


print(max(list(d.values())))

# Your code here
a,b=map(int,input().split())
l=list(map(int,input().split()))

d={
    0:0,
    1:1
}
sum=0
# for i in range(b):
#     d[i]=i

# print(d)

for j in range(1,b):
    for i in l:
        sum+=j^i
    if(sum>d[1]):
        d[0]=d[1]
        d[1]=sum
    sum=0

# print(d)
print(max(list(d.values())))

# Your code here
a,b=map(int,input().split())
l=list(map(int,input().split()))

flag=0
sum=0
# for i in range(b):
#     d[i]=i

# print(d)

for j in range(1,b):
    for i in l:
        sum+=j^i
    if(sum>flag):
        flag=sum
    sum=0

# print(d)
print(flag)