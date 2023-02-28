from itertools import permutations
given=input().split()

ans=list(permutations(given[0],int(given[1])))
ans.sort()

for i in ans:
    print("".join(i))