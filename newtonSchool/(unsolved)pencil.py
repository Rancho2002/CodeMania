# Your code here
wish=list(map(int,input().split()))
N=wish[0] #pencil stash
stash=[]
merged=[] #took merged of two element of stash 
time=0
for i in range(N):
    a=int(input())
    stash.append(a)

for x in stash:
    for y in stash:
        merged.append(x+y)

for j in range(1,len(wish)):
    for k in range(len(stash)):

        if(wish[j]-stash[k]==1):
            time+=1
        if(stash[k]-wish[j]==1):
            time+=1
        if(abs(wish[j]-(merged[k]+merged[j]))<5):
            time+=10+(wish[j]-(merged[k]+merged[j]))

print(time)
        
