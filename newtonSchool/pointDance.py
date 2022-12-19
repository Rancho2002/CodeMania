# Your code here
checkpt, total=map(int,input().split())
cords=list(map(int,input().split()))
cords.sort()
place=0
l=[0]
for i in range(1,total):
    l.append(abs(cords[i-1]-cords[i]))

l.sort()
# print(l)
# print(total-checkpt)
for i in range(total-checkpt+1):
    place+=l[i]
print(place)