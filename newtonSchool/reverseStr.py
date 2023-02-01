# Your code here
def rev(s):
    s=list(s)
    s.reverse()
    return "".join(s)

a,b=map(int,input().split())
s=input()

print(s[0:a-1]+rev(s[a-1:b])+s[b:])