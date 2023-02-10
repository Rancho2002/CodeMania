# Your code here
A,B,C,K=map(int,input().split())
if(A>=K):
    print(K)
elif(A+B>=K):
    print(A*1+B*0)
elif(A+B < K):
    temp=A+B
    C=K-temp
    print(C*-1+A)