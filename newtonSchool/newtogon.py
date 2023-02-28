# Your code here
a=int(input())
sides=list(map(int,input().split()))
temp=sides.copy()

flag=False
for i in sides:
    temp.remove(i)
    print(temp)
    if(i>=sum(temp)):
        flag=True
    temp=sides.copy()

if(flag): print("No")
else: print("Yes")


#! concept
'''
# print(temp)
# temp.remove(sides[0])
# print(sides)
# sides=temp
# print(temp)
'''