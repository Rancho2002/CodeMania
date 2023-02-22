# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d=OrderedDict()
for i in range(int(input())):
    l=input().split()
    a=" ".join(l[0:2]) if len(l)>2 else l[0]
    b=int(l[2]) if(len(l)>2) else int(l[1])
    if a in d:
        d[a]=d[a]+int(b)
    else:
        d[a]=int(b)
        
for j in d:
    print(j,d[j])
    