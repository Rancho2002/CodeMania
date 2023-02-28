for i in range(int(input())):
    total,balance=map(int,input().split())
    l=list(map(int,input().split()))
    for j in range(len(l)):
        temp=balance
        balance=balance-l[j]
        if(balance>=0):
            flag=1
        else:
            flag=0
            balance=temp
        print(flag,end='')
    print()