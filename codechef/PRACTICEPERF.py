# cook your dish here
l=[]
count=0
a,b,c,d=map(int,input().split())
l.append(a)
l.append(b)
l.append(c)
l.append(d)
for i in range(len(l)):
    if(l[i]>=10):
        count+=1
print(count)
