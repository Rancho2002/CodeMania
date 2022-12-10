for i in range(int(input())):
    l=[]
    input()
    a=list(input().strip())
    for j in a:
        if(a.count(j)>1):
            l.append(a.count(j))
        else:
            l.append(0)
    print(max(l))
    # a=[]
