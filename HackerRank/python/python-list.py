if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        a=list(input().split())
        if(len(a)==3):
            a[1]=int(a[1])
            a[2]=int(a[2])
        elif(len(a)==2):
            a[1]=int(a[1])
        # print(a)
        if(a[0]=="insert"):
            l.insert(a[1],a[2])
        if(a[0]=="remove"):
            l.remove(a[1])
        if(a[0]=="append"):
            l.append(a[1])
            # print(l)
        if(a[0]=="sort"):
            l.sort()
        if(a[0]=="reverse"):
            l.reverse()
        if(a[0]=="pop"):
            l.pop()
        if(a[0]=="print"):
            print(l)