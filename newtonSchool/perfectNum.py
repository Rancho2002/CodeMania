def check(x:int)->bool:
    ans=0
    for i in range(1,x//2+1):
        if(x%i==0):
            ans+=i
    if(ans==x):
        return True
    return False

n=int(input())
print(n**2 if(check(n)) else -1)