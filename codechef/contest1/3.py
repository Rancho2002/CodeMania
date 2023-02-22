for i in range(int(input())):
    N,X=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    for _ in range(N-X):
        l.pop()
        
    ans=min(l)-1
    print(ans)
# https://www.codechef.com/START78D/problems/CUTOFF