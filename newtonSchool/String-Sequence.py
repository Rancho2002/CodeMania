# Your code here
s="abcdefghijklmnopqrstuvwxyz"
l=list(map(int,input().split()))
for i in l:
    print(s[i-1],end="")