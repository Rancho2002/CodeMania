for i in range(int(input())):
    a,b=map(int,input().split())
    if(a%2!=0 and b%2==0):
        print("NO")
    else:
        print("YES")