# Your code here
N,K=map(int,input().split())

while(int(K)):
    if(int(N)%200==0):
        N=int(N)
        N=N//200
    else:
        N=str(N)
        N=N+"200"
    K-=1
print(N)