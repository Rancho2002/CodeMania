# Your code here
def swap(s,a,b):
    if s[a]==s[b]:
        return s
    else:
        s=list(s)
        s[a],s[b]=s[b],s[a]
        return ''.join(s)
 

s=input()
t=input()

for i in range(len(s)-1):
    if(s[i]==t[i]):
        continue
    else:
        s=swap(s,i,i+1)

if(s==t):
    print("Yes")
else:
    print("No")