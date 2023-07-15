def solve(arr,difference):
    c=1
    d:dict[int,int]={}
    k=1e4+1
    for i in range(len(arr)):
        if arr[i]-difference in d and (k==1e4+1 or arr[i]-difference==k):
            # print(arr[i])
            c+=1
            k=arr[i]
        d[arr[i]]=1
        # print(d)
    
    return c

print(solve([16,-4,-6,-11,-8,-9,4,-11,15,15,-9,11,7,-7,10,-16,4],3))
# print(solve([16,-4,-6,-11,*,-9,4,-11,15,15,-9,11,7,-7,*,-16,4],3))