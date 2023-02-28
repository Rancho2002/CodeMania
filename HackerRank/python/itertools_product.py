# Enter your code here. Read input from STDIN. Print output to STDOUT
A=list(map(int,input().split()))
B=list(map(int,input().split()))

for i in range(len(A)):
    for j in range(len(B)):
        print("(",A[i],", ",B[j],")",end=" ",sep="")