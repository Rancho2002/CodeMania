for i in range(int(input())):
    l=[]
    a=int(input())
    for j in range(1,a+1):
        l.append(j)
    # print(l)
    while(len(l)!=0):
        l.reverse()
        b=l.pop()
    print(b)