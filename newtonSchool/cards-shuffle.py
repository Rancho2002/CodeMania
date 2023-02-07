# Your code here
from collections import Counter
n=int(input())
l=list(map(int,input().split()))
l=Counter(l)
chk=min(l.values())
for i in l:
    if l[i]==chk:
        print(i)
        break
    