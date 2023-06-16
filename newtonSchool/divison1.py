# Your code here
def isOdd(n: int) -> bool:
    return (n & 1) != 0

def solve(n: int) -> bool:
    if isOdd(n):
        return True

    for i in range(2,int(n**0.5)+1):
        if(n%i==0 and isOdd(i))or(n%(n//i)==0 and isOdd(n//i)):
            return True
    return False

n = int(input())

if solve(n):
    print("YES")
else:
    print("NO")