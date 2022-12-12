a,b=input().split()
l=list(map(int,input().split()))
l.sort(reverse=True)
# l= [-40, -10, 5, 20, 80]
# l.remove(-40)
newL=[]
diff = lambda l: abs(l-0)
for i in range(int(b)):
    res=min(l,key=diff)
    newL.append(res)
    l.remove(res)
# print(newL)
distance=0
removeE=[]
for j in range(len(newL)):
    # print(newL[j])
    if(newL[j]<0):
        # print(newL[j])
        distance+=abs(newL[j]*2)
        removeE.append(newL[j])

for m in range(len(removeE)):
    newL.remove(removeE[m])

# print(distance)
# print(newL)

distance+=newL[0]
for k in range(len(newL)-1):
        # 6 + 1
        # 7 + (2-1)
        # 8 + (3-2)
        # 9 + (4-3)
        # 10
    distance+=newL[k+1]-newL[k]
print(distance)

