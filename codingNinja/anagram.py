def anagramMapping(n: int, a: list[int], b: list[int]) -> list[int]:
    # write your code here
    d={}
    for i in range(len(b)):
        if(b[i] not in d):
            d[b[i]]=i
    ans=[]
    for i in range(len(a)):
        ans.append(d.get(a[i]))
    return ans

print(anagramMapping(5,[10,20,30,40,50],[20,10,40,50,30]))