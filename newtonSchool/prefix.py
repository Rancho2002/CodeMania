# Your code here
def prefix(s,t):
    if(len(s)<=len(t) and s==t[0:len(s)]): print("Yes")
    else: print("No")
s=input()
t=input()
prefix(s,t)