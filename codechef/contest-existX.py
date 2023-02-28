x=[]
for i in range(11):
    x.append(i)
# print(x)

for j in range(int(input())):
    a,b,c=map(int,input().split())
    for k in range(len(x)):
        if(a^x[k]+b^x[k]==c^x[k]):
            flag=True
            # print(x[k],"true")
            break
        else:
            flag=False
    if(flag):
        print("YES")
    else:
        print("NO")
    