n=int(input())
l=list(map(int,input().split()))
temp=0
for i in range(1,101):
    temp=0
    for j in range(n):
        temp=temp+(i-l[j])**2
    if(i==1 or temp<comp):    
        comp=temp
        
print(comp)

# https://my.newtonschool.co/playground/code/z5r4ilbk329a