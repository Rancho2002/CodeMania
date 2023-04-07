# cook your dish here
# C-2 o-1 d-1 e-2 h-1 f-1
for i in range(int(input())):
    n=int(input())
    ans=c=o=d=e=h=f=0
    for j in range(n):
        s=input()
        c+=s.count("c")
        o+=s.count("o")
        d+=s.count("d")
        e+=s.count("e")
        h+=s.count("h")
        f+=s.count("f")
        
    # print([c,o,d,e,h,f])
        if c//2>=1 and o>=1 and d>=1 and e//2>=1 and h>=1 and f>=1:
            ans= min(c,o,d,e,h,f)
        
    print(ans)