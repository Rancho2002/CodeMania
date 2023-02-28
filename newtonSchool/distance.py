# Your code here
def solve():
    pts=sorted(list(map(int,input().split())))
    pts.pop()
    print(sum(pts))

solve()