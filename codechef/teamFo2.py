# cook your dish here
x=int(input())
c=[]
for i in range(x):
    y=int(input())
    for j in range(y):
        # l=[]
        l=map(int, input().split())
        l=[int(x) for x in l]
        # print(l)
        for i in range(len(l)):
            c.append(l[i])
        # print(c)
    if 1 in c and 2 in c and 3 in c and 4 in c and 5 in c:
        print("YES")
    else:
        print("NO")
    c=[]
        
    