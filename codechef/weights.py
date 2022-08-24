# cook your dish here
a=int(input())
for i in range(a):
    b,c,d,e=map(int, input().split())
    flag=0
    if(b==c or b==d or b==e or b==(c+d) or b==(c+e) or b==(d+e) or b==(c+d+e)):
        print("YES")
    else:
        print("NO")
                