# Your code here
def solve(a,b):
    for i in range(b-a+1,b+a):
        print(i,end=" ")

a,b=map(int,input().split())
solve(a,b)