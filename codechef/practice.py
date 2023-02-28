# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
p=1
for i in range(a):
    int(input())
    l=list(map(int,input().split()))
    for j in range(len(l)):
        p=p*l[j]
        # print(p)
    if(p<0):
        print(1)
    else:
        print(0)
    p=1