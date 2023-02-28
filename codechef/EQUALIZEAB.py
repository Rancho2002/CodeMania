a=int(input())
for i in range(a):
    a,b,x=map(int,input().split())
    flag=0
    temp1=a
    temp2=b
    if(a==b):
        print("YES")
    else:
        while(a!=b and a>=1 and b>=1):
            a=a+x 
            b=b-x
            if(a==b):
                flag=1
                break
            else:
                a=temp1
                b=temp2
                while(a!=b and a>=1 and b>=1):
                    a=a-x 
                    b=b+x
                    if(a==b):
                        flag=1
                        break
        if(flag):
            print('YES')
        else:
            print('NO')

#! Wrong answer :(