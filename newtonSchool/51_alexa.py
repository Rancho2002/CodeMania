# Your code here
s=list(input())
s.reverse()
s="".join(s)
if "a" in s: print(len(s)-s.index("a"))
else: print(-1)
