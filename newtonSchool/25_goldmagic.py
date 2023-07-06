# Your code here
def magic(gold,n):
    gold.sort()
    s=(gold[0]+gold[1])/2
    for i in range(2,n):
        s=s+gold[i]
        s=s/2
    return s
n=int(input())
gold=list(map(int,input().split()))

print(f"{magic(gold,n):.8f}")

'''
# Your code here
n=int(input())
gold=list(map(int,input().split()))
gold.sort()
s=(gold[0]+gold[1])/2
for i in range(2,n):
    s=s+gold[i]
    s=s/2
print(format(s,".8f"))
'''