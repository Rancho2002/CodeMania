def countFrequency(n: int, m: int, edges: list[int]):
    d={}
    for i in range(1,m+1):
        d[i]=0
    
    for i in edges:
        if i in d:
            d[i]+=1
    
    ans=[]
    for i in range(1,n+1):
        ans.append(d[i])
    
    return ans