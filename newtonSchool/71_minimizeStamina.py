n=int(input())
l=list(map(int,input().split()))
temp=0
for i in range(min(l),max(l)):
    temp=0
    for j in range(n):
        temp=temp+(i-l[j])**2
    if(i==min(l) or temp<comp):    
        comp=temp
        
print(comp)
# https://my.newtonschool.co/playground/code/z5r4ilbk329a