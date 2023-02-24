# Your code here
l=list(map(int,input().split()))
l1=list(set(l))
if(l.count(l1[0])==3 and l.count(l1[1])==2) or (l.count(l1[0])==2 and l.count(l1[1])==3):
    print("Yes")
else:
    print("No")