# Your code here
a,b=map(int,input().split())
flag=False

while(a):
    d=a%10
    e=b%10
    chk=(d+e)%10
    if(chk<a%10 and chk<b%10):
        flag=True
        break
    else:
        a=a//10
        b=b//10
print("Hard" if flag else "Easy")