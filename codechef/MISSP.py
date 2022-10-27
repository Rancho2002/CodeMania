for i in range(int(input())):
    count=0
    a=int(input())
    l=[]
    for k in range(a):
        l.append(int(input()))
    for j in range(len(l)):
        if(l[j]%2!=0):
            # print(l[j])
            count+=1
    print(count)
    l=[]