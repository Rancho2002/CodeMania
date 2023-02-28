# Your code here
def solve(s,t):
    a=b=c=[x for x in range(0,101)]
    count=0
    for i in a:
        for j in b:
            for k in c:
                if(i+j+k<=s and i*j*k<=t):
                    count+=1
    return count

s,t=map(int,input().split())
print(solve(s,t))