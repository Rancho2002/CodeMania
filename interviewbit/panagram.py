def solve(A):
    d={}
    for i in A:
        for j in range(len(i)):
            if(i[j] in d):
                d[i[j]]+=1
            else:
                d[i[j]]=1
    print(d)
    return 1 if (len(list(d.keys()))==26) else 0


print(solve(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]))