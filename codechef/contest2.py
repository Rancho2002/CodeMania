# a=list(input().strip())
a=input()
result=[]
for i in range(len(a)):
    for j in range(i + 1, len(a) + 1):
        result.append(a[i: j])
print(len(result))