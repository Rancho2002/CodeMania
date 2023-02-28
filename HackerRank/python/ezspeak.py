# https://www.codechef.com/submit/EZSPEAK
# cook your dish here
x=int(input())

for i in range(x):
    b=int(input())
    a=input()
    flag=0
    count=0
    for i in range(len(a)):
        if(count>=4):
            flag=1
            break
        else:
            if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
                count=0
                continue
            else:
                count+=1
    if(flag):
        print("NO")
    else:   
        print("YES")
        
