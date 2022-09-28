# https://www.codechef.com/submit/MINCOINS

# cook your dish here
a=int(input())
l=[]
for i in range(a):
    b=int(input())
    if(b%5!=0 and b%10!=0):
        print(-1)
    else:
        if(b%5==0):
            l.append(int(b/5))
        if(b%10==0):
            l.append(int(b/10))
        l.append(int(b/10)+ int((b%10)/5))
        # print(l)
        print(min(l))
        l=[]