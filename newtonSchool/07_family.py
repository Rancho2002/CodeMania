# https://my.newtonschool.co/playground/code/ivfg9mx69lbk
# Your code here
# family=int(input())
# l=list(map(int,input().split()))
# for i in range(1,family+1):
#     print(l.count(i))

# family=int(input())
# N={}
# for i in range(1,family+1):
    # N[i]=0

# l=list(map(int,input().split()))

# for j in l:
#     if(j==N.keys):
#         N[j]+=1
# print(N.keys(0))

# Your code here
n=int(input())
l=list(map(int,input().split()))
d ={}
for i in l:
    if i in d :
        d[i] = d[i]+1
        # print(d,"call hua1")
    else:
        d[i]=1
        # print(d,"call hua2")

# print(d)

for i in range(1,n+1):
    if i in d:
        pass
    else :
        d[i]=0
        
for i in range(1,n+1):
    print(d[i])